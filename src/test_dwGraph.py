"""
File: test_dwGraph.py
Author: Slobo Matic
Date: 11/08/2016

Description: Unit tests used for Digital Wallet functionality.

Usage: python test_dwGraph.py -v
"""

import unittest
from dwGraph import Queue, Vertex, Graph
 
class test_dwGraph(unittest.TestCase):

	# run before each test method 
	def setUp(self):
		pass

	# tests on simple graph with few edges 
	def test_basicGraph(self):
		g = Graph()
		for i in range(8):
			g.addVertex(i)
		# check the number of vertices is 8
		self.assertEqual(8,g.numVertices)
		g.addVertex(5) 
		# check the number of vertices is still 8
		self.assertEqual(8,g.numVertices)
		g.addEdge(0,1,1)
		g.addEdge(1,0,1)
		g.addEdge(2,3,1)
		g.addEdge(3,2,1)
		g.addEdge(4,5,1)
		g.addEdge(5,4,1)
		g.addEdge(6,7,1)
		g.addEdge(7,6,1)
		# check the number of edges is 8
		self.assertEqual(2*4,g.numDirectedEdges()) 
		g.addEdge(4,5)
		# check the number of edges is still 8
		self.assertEqual(2*4,g.numDirectedEdges()) 
		for v in g: self.assertEqual([0,'white',None],[v.degree,v.visited,v.parent])    
		# check the breadth-first search degree 4
		self.assertEqual(set([0,1]),g.bfs(1,4))
		# check the breadth-first search precondition / postcondition
		for v in g: self.assertEqual([0,'white',None],[v.degree,v.visited,v.parent])    
		# check the breadth-first search degree 4
		self.assertEqual(set([6,7]),g.bfs(6,4))
		# check the breadth-first search precondition / postcondition
		for v in g: self.assertEqual([0,'white',None],[v.degree,v.visited,v.parent])    
		# check the friend degree 4
		auxSet = [2,3]
		for i in range(8):
			if i in auxSet:
				self.assertTrue(g.friendsDegree(2,i,4))
			else:
				self.assertFalse(g.friendsDegree(2,i,4))
		# check the breadth-first search precondition / postcondition
		for v in g: self.assertEqual([0,'white',None],[v.degree,v.visited,v.parent])    

	# tests on tree 
	def test_tree(self):	
		g = Graph()
		for i in range(17):
			g.addVertex(i)
		# check the number of vertices is 8
		self.assertEqual(17,g.numVertices)
		g.addEdge(0,1), g.addEdge(1,0)
		g.addEdge(0,2), g.addEdge(2,0)
		g.addEdge(0,3), g.addEdge(3,0)
		g.addEdge(1,4), g.addEdge(4,1)
		g.addEdge(1,5), g.addEdge(5,1)
		g.addEdge(2,6), g.addEdge(6,2)
		g.addEdge(3,7), g.addEdge(7,3)
		g.addEdge(5,8), g.addEdge(8,5)
		g.addEdge(6,9), g.addEdge(9,6)
		g.addEdge(6,10), g.addEdge(10,6)
		g.addEdge(6,11), g.addEdge(11,6)
		g.addEdge(7,12), g.addEdge(12,7)
		g.addEdge(7,13), g.addEdge(13,7)
		g.addEdge(10,14), g.addEdge(14,10)
		g.addEdge(14,15), g.addEdge(15,14)
		g.addEdge(14,16), g.addEdge(16,14)
		# check the number of edges is 8
		self.assertEqual(32,g.numDirectedEdges()) 
		# check the breadth-first search precondition / postcondition
		for v in g: self.assertEqual([0,'white',None],[v.degree,v.visited,v.parent])    
		# check the breadth-first search degree 1
		self.assertEqual(set(range(4)),g.bfs(0,1))
		# check the breadth-first search precondition / postcondition
		for v in g: self.assertEqual([0,'white',None],[v.degree,v.visited,v.parent])    
		# check the breadth-first search degree 1
		self.assertEqual(set([3,7,12,13]),g.bfs(7,1))
		# check the friend degree 1
		auxSet = [3,7,12,13]
		for i in range(17):
			if i in auxSet:
				self.assertTrue(g.friendsDegree(7,i,1))
			else:
				self.assertFalse(g.friendsDegree(7,i,1))
		# check the breadth-first search precondition / postcondition
		for v in g: self.assertEqual([0,'white',None],[v.degree,v.visited,v.parent])    
		self.assertEqual(32,g.numDirectedEdges()) 
		# check the breadth-first search precondition / postcondition
		for v in g: self.assertEqual([0,'white',None],[v.degree,v.visited,v.parent])    
		# check the breadth-first search degree 2
		self.assertEqual(set(range(8)),g.bfs(0,2))
		# check the breadth-first search precondition / postcondition
		for v in g: self.assertEqual([0,'white',None],[v.degree,v.visited,v.parent])    
		# check the breadth-first search degree 2
		self.assertEqual(set([0,3,7,12,13]),g.bfs(7,2))
		# check the breadth-first search precondition / postcondition
		for v in g: self.assertEqual([0,'white',None],[v.degree,v.visited,v.parent])    
		# check the breadth-first search degree 2
		self.assertEqual(set([2,6,9,10,11,14,15,16]),g.bfs(10,2))
		# check the friend degree 2
		auxSet = [2,6,9,10,11,14,15,16]
		for i in range(17):
			if i in auxSet:
				self.assertTrue(g.friendsDegree(10,i,2))
			else:
				self.assertFalse(g.friendsDegree(10,i,2))
		# check the breadth-first search precondition / postcondition
		for v in g: self.assertEqual([0,'white',None],[v.degree,v.visited,v.parent])    
		# check the breadth-first search degree 4
		self.assertEqual(set(range(15)),g.bfs(0,4))
		# check the breadth-first search precondition / postcondition
		for v in g: self.assertEqual([0,'white',None],[v.degree,v.visited,v.parent])    
		# check the breadth-first search degree 4
		self.assertEqual(set(range(14)),g.bfs(1,4))
		# check the breadth-first search precondition / postcondition
		for v in g: self.assertEqual([0,'white',None],[v.degree,v.visited,v.parent])    
		# check the breadth-first search degree 4
		self.assertEqual(set([2,6,9,10,11,14,15,16]),g.bfs(16,4))
		# check the friend degree 4
		auxSet = [2,6,9,10,11,14,15,16]
		for i in range(17):
			if i in auxSet:
				self.assertTrue(g.friendsDegree(16,i,4))
			else:
				self.assertFalse(g.friendsDegree(16,i,4))
		# check the breadth-first search precondition / postcondition
		for v in g: self.assertEqual([0,'white',None],[v.degree,v.visited,v.parent])    

	# tests on complete graph 
	def test_completeGraph(self):	
		g = Graph()
		n = 10
		for i in range(n):
			g.addVertex(i)
		# check the number of vertices is n
		self.assertEqual(n,g.numVertices)
		for v1 in range(n):
			for v2 in range(n): 
				if v1 != v2:
					g.addEdge(v1,v2)
		# check the number of edges is n*(n-1)
		self.assertEqual(n*(n-1),g.numDirectedEdges()) 
		# check the breadth-first search precondition / postcondition
		for v in g: self.assertEqual([0,'white',None],[v.degree,v.visited,v.parent])    
		# check the breadth-first search degree 1
		self.assertEqual(set(range(n)),g.bfs(0,1))
		# check the breadth-first search precondition / postcondition
		for v in g: self.assertEqual([0,'white',None],[v.degree,v.visited,v.parent])    
		# check the breadth-first search degree 2
		self.assertEqual(set(range(n)),g.bfs(n-1,2))
		# check the breadth-first search precondition / postcondition
		for v in g: self.assertEqual([0,'white',None],[v.degree,v.visited,v.parent])    
		# check the breadth-first search degree 4
		self.assertEqual(set(range(n)),g.bfs(0,4))
		# check the breadth-first search precondition / postcondition
		for v in g: self.assertEqual([0,'white',None],[v.degree,v.visited,v.parent])    

	# tests on graph built from input file containing Digital Wallet transactions
	def test_readFromFile(self):
		folderName = r'./paymo_input'
		transactionFileName = r'/batch_payment.csv' #3938414

		infile = open(folderName+transactionFileName, "r") #, encoding = 'utf-8')
		lineRead = len(infile.readlines())
		infile.close()

		g = Graph()
		repeatFrom, repeatTo, repeatEdge, lineError, selfVertex = g.readBatchFile(folderName+transactionFileName,False)
		# repeatFrom, repeatTo, repeatEdge, lineError, selfVertex = g.readBatchFile(folderName+transactionFileName,True)

		# check the number of read vertices matches with read lines w/o header line
		self.assertEqual(2*(lineRead-1),g.numVertices+repeatFrom+repeatTo+2*lineError) 
		# check the number of read edges matches with read lines w/o header line
		self.assertEqual(lineRead-1,g.numDirectedEdges()/2+repeatEdge+lineError+selfVertex)

		# check the breadth-first search precondition / postcondition
		for v in g: self.assertEqual([0,'white',None],[v.degree,v.visited,v.parent])    
		# check the breadth-first search degree 0
		self.assertEqual(set([30909]),g.bfs(30909,0))
		# check the breadth-first search precondition / postcondition
		for v in g: self.assertEqual([0,'white',None],[v.degree,v.visited,v.parent])    
		# check the breadth-first search degree 1
		self.assertEqual(set([70642, 30909, 33600, 4097, 2437, 8199, 15242, 5900, 15310, 25049, 46618, 10976, 48993, 26466, 10600, 29298, 4916, 9655]),g.bfs(30909,1))
		set2 = set([30909])
		for id in [70642, 33600, 4097, 2437, 8199, 15242, 5900, 15310, 25049, 46618, 10976, 48993, 26466, 10600, 29298, 4916, 9655]:
			set1 = g.bfs(id,1)
			set2 = set2|set1
		# check the breadth-first search precondition / postcondition
		for v in g: self.assertEqual([0,'white',None],[v.degree,v.visited,v.parent])    
		# check the breadth-first search degree 2
		self.assertEqual(set2,g.bfs(30909,2))
		# check the breadth-first search precondition / postcondition
		for v in g: self.assertEqual([0,'white',None],[v.degree,v.visited,v.parent])    
		# check the friend degree 2
		for i in set2:
			self.assertTrue(g.friendsDegree(30909,i,2))
		# check the breadth-first search precondition / postcondition
		for v in g: self.assertEqual([0,'white',None],[v.degree,v.visited,v.parent])    

if __name__ == '__main__':
    unittest.main()
