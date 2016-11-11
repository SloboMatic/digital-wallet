"""/
File: dwGraph.py
Author: Slobo Matic
Date: 11/08/2016

Description: Digital Wallet main code and classes

Usage: python dwGraph.py batchFile streamFile output1File output2File outputFile3 outputFile4
"""

import sys
import time
import datetime

# Basic queue class used for breadth first search to traverse verteces
class Queue:
    def __init__(self):
        self.items = []

    def isEmpty(self):
        return self.items == []

    def enqueue(self, item):
        self.items.insert(0,item)

    def dequeue(self):
        return self.items.pop()

    def size(self):
        return len(self.items)

    def __str__(self):
        return str(self.items)

# Basic vertex class representing Digital Wallet users
# Initialized after each breadth-first search 
class Vertex:
    def __init__(self,key):
        self.id = key
        self.lastPayDateTime = datetime.datetime.strptime('1970-01-01 00:00:00', '%Y-%m-%d %H:%M:%S') 
        self.paymentCurrentMinute = 0 
        self.degree = 0
        self.parent = None   
        self.visited = 'white'
        self.connectedTo = {}

    def initBFS(self):
        self.degree = 0
        self.parent = None   
        self.visited = 'white'    

    def setPayment(self,payDateTime,payment):
        self.lastPayDateTime = payDateTime 
        self.paymentCurrentMinute = payment

    def getDegree(self):        
        return self.degree

    def setDegree(self,degree):
        self.degree = degree

    def getParent(self):        
        return self.parent

    def setParent(self,parent):
        self.parent = parent

    def getVisited(self):        
        return self.visited

    def setVisited(self,visited):
        self.visited = visited

    def addNeighbor(self,nbr,weight=0):
        self.connectedTo[nbr] = weight

    def __str__(self):
        return str(self.id) + ' connectedTo: ' + str([(x.id,self.connectedTo[x]) for x in self.connectedTo])

    def getConnections(self):
        return self.connectedTo.keys()

    def getId(self):
        return self.id

    def getWeight(self,nbr):
        return self.connectedTo[nbr]

# Graph class where edges represent Digital Wallet transactions
class Graph:
    def __init__(self):
        self.vertList = {}
        self.numVertices = 0

    def addVertex(self,key,):
        if key not in self.vertList:
            self.numVertices = self.numVertices + 1
            newVertex = Vertex(key)
            self.vertList[key] = newVertex
            return newVertex
        else:
            return None

    def getVertex(self,n):
        if n in self.vertList:
            return self.vertList[n]
        else:
            return None

    def __contains__(self,n):
        return n in self.vertList

    def addEdge(self,f,t,cost=0):
        if f not in self.vertList:
            nv = self.addVertex(f)
        if t not in self.vertList:
            nv = self.addVertex(t)
        self.vertList[f].addNeighbor(self.vertList[t], cost)

    def getVertices(self):
        return self.vertList.keys()

    def numDirectedEdges(self):
        edges = 0
        for v in self:
            edges += len(v.getConnections())
        return edges

    def __iter__(self):
        return iter(self.vertList.values())

    def __str__(self):
        return str(self.numVertices) + ' vertices: ' + str([x for x in self.vertList])

    # read input batch file, process transactions, add new vertices and edges
    def readBatchFile(self,fileName,verbose):
        infile = open(fileName, "r") #, encoding = 'utf-8')
        infile.readline()   # ignore the first line, i.e. skip the headers

        t0 = time.time()
        # variables used in unit testing
        lineRead, lineError, repeatFrom, repeatTo, repeatEdge, selfVertex = 0, 0, 0, 0, 0, 0
        for line in infile:
            foundFrom, foundTo = False, False
            lineRead += 1
            col = line.split(',')
				# some lines might contain data of wrong type 
            try:
                l0, l1, l2, l3 = datetime.datetime.strptime(col[0], '%Y-%m-%d %H:%M:%S'), int(col[1]), int(col[2]), float(col[3])
            except (IndexError,ValueError):
                if verbose:
                    print('Oops!  That was not a valid entry at line ',lineRead+1,': ',line)
                lineError += 1
                continue
            # add first vertex if new
            if self.addVertex(l1) == None:
                repeatFrom += 1
                foundFrom = True
            # add second vertex if new
            if self.addVertex(l2) == None:
                repeatTo += 1
                foundTo = True
            # for the receiving user set the date and time of last payment as well as the total payment in the current minute
            lPDT = self.getVertex(l2).lastPayDateTime
            if lPDT.date() == l0.date() and lPDT.hour == l0.hour and lPDT.minute == l0.minute:
                # if previous payment to this user was in the same minute add the new payment    	
                self.getVertex(l2).setPayment(l0,self.getVertex(l2).paymentCurrentMinute+l3)
            else:
                # if previous payment to this user was not in the same minute just take the new payment    	
                self.getVertex(l2).setPayment(l0,l3)  
            # add edges
            if self.getVertex(l2) in self.getVertex(l1).getConnections():
                repeatEdge += 1
            if l1 == l2:
                selfVertex += 1
            else:
                self.addEdge(l1,l2,l3)
                self.addEdge(l2,l1,l3)

        if verbose:
            print('graph read elapsed time : ', time.time() - t0)
            print('read '+str(lineRead)+' lines')
            print(str(repeatFrom)+' repeated From vertices, '+str(repeatTo)+' repeated To vertices, '+str(repeatEdge)+' repeated edges '+str(selfVertex)+' self vertices')

        infile.close()
        return repeatFrom, repeatTo, repeatEdge, lineError, selfVertex

    # read input stream file, process transactions, write warnings to output file
    def writeStreamFile(self,fileName,outputFileName,feature,verbose):
        infile = open(fileName, "r") #, encoding = 'utf-8')
        infile.readline()   # ignore the first lien, i.e. skip the headers

        outfile = open(outputFileName, "w") #, newline="\n", encoding="utf-8")

        t0 = time.time()
        lineRead, lineError, repeatFrom, repeatTo, repeatEdge, selfVertex = 0, 0, 0, 0, 0, 0
        for line in infile:
            lineRead += 1
            # if lineRead%1000 == 0:
            #     print(lineRead)
            col = line.split(',')
				# some lines might contain data of wrong type 
            try:
                l0, l1, l2, l3 = datetime.datetime.strptime(col[0], '%Y-%m-%d %H:%M:%S'), int(col[1]), int(col[2]), float(col[3])
            except (IndexError,ValueError):
                if verbose:
                    print('Oops!  That was not a valid entry at line ',lineRead+1,': ',line)
                outfile.write('unverified'+'\n')
                lineError += 1
                continue
            if self.addVertex(l1) == None:
                repeatFrom += 1
            if self.addVertex(l2) == None:
                repeatTo += 1
            # for the receiving user set the date and time of last payment as well as the total payment in the current minute
            lPDT = self.getVertex(l2).lastPayDateTime
            if lPDT.date() == l0.date() and lPDT.hour == l0.hour and lPDT.minute == l0.minute:
                # if previous payment to this user was in the same minute add the new payment    	
                self.getVertex(l2).setPayment(l0,self.getVertex(l2).paymentCurrentMinute+l3)
            else:
                # if previous payment to this user was not in the same minute just take the new payment    	
                self.getVertex(l2).setPayment(l0,l3)

            flag = False
            if feature == 1:
                if self.getVertex(l2) in self.getVertex(l1).getConnections() or l1 == l2:
                    repeatEdge += 1
                    flag = True
            if feature == 2:
                for vertex1 in self.getVertex(l1).getConnections():
                    vertex2 = self.getVertex(l2) 
                    if vertex2 == vertex1 or vertex2 in vertex1.getConnections():
                         flag = True
                         break
            if feature == 3:
                if self.friendsDegree(l1,l2,4):
                    flag = True
            if feature == 4:
                if self.getVertex(l2).paymentCurrentMinute > 100 and self.getVertex(l2).paymentCurrentMinute < 10000:
                    flag = True

            if flag or l1 == l2:
                outfile.write('trusted'+'\n')
            else:
                outfile.write('unverified'+'\n')

            if l1 == l2:
                selfVertex += 1
            else:
                self.addEdge(l1,l2,l3)
                self.addEdge(l2,l1,l3)

        if verbose:
            print('graph read elapsed time : ', time.time() - t0)
            print('read '+str(lineRead)+' lines')
            print(str(repeatFrom)+' repeated From vertices, '+str(repeatTo)+' repeated To vertices, '+str(repeatEdge)+' repeated edges '+str(selfVertex)+' self vertices')

        infile.close()
        outfile.close()
        return repeatFrom, repeatTo, repeatEdge, lineError, selfVertex

	 # breadth-first search (used in testing)
    def bfs(self, root, relDegree = float('inf')):
        friends = set([])
        vertQueue = Queue()
        vertQueue.enqueue(self.getVertex(root))
        while (vertQueue.size() > 0):
            currentVert = vertQueue.dequeue()
            if currentVert.getDegree() > relDegree:
                break
            for nbr in currentVert.getConnections():
                if (nbr.getVisited() == 'white'):
                    nbr.setVisited('gray')
                    nbr.setDegree(currentVert.getDegree() + 1)
                    nbr.setParent(currentVert)
                    vertQueue.enqueue(nbr)
            currentVert.setVisited('black')
            friends.add(currentVert.getId())
        # clean up
        for id in friends:
            Vert = self.getVertex(id)
            Vert.initBFS()
        currentVert.initBFS()
        while (vertQueue.size() > 0):
            currentVert = vertQueue.dequeue()
            currentVert.initBFS()
        return friends

    # returns whether a vertex is in the circle of friends of degree reldegree
    def friendsDegree(self, root, leaf, relDegree = float('inf')):
        flag = False
        friends = set([])
        vertQueue = Queue()
        vertQueue.enqueue(self.getVertex(root))
        while (vertQueue.size() > 0):
            currentVert = vertQueue.dequeue()
            if currentVert.getDegree() > relDegree:
                break
            if leaf == currentVert.getId():
                flag = True
                break
            for nbr in currentVert.getConnections():
                if (nbr.getVisited() == 'white'):
                    nbr.setVisited('gray')
                    nbr.setDegree(currentVert.getDegree() + 1)
                    nbr.setParent(currentVert)
                    vertQueue.enqueue(nbr)
            currentVert.setVisited('black')
            friends.add(currentVert.getId())
        for id in friends:
            Vert = self.getVertex(id)
            Vert.initBFS()
        currentVert.initBFS()
        while (vertQueue.size() > 0):
            currentVert = vertQueue.dequeue()
            currentVert.initBFS()
        return flag

def main():

    # parse the input parameters: 
    #    input batch file, input stream file, output file for feature 1, output file for feature 2, output file for feature 3, output file for feature 4
    batchFileName = sys.argv[1] 
    streamFileName = sys.argv[2] 
    output1FileName = sys.argv[3] 
    output2FileName = sys.argv[4] 
    output3FileName = sys.argv[5] 
    output4FileName = sys.argv[6] 

    # create the digital wallet graph
    g = Graph()
    # process input batch file, for verbose output change second argument to True
    g.readBatchFile(batchFileName,False)

    # Feature 1: trusted if previously paid. Process transactions from input stream file and generate output1.txt
    g.writeStreamFile(streamFileName,output1FileName,1,False)

    # Feature 2: trusted if in friend network of degree 2. Process transactions from input stream file and generate output2.txt
    g.writeStreamFile(streamFileName,output2FileName,2,False)

    # Feature 3: trusted if in friend network of degree 4. Process transactions from input stream file and generate output3.txt
    g.writeStreamFile(streamFileName,output3FileName,3,False)

    # Feature 4: trusted if in the current time interval payee received an amount in the certain range. Process transactions from input stream file and generate output4.txt
    g.writeStreamFile(streamFileName,output4FileName,4,False)

if __name__ == '__main__':
    main()
 