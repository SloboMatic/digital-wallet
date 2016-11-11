## Digital Wallet

Python solution to the digital wallet coding challenge.

The code is based on graph, vertex and queue data structures with slight modifications for methods that address challenge requirements.

The Digital Wallet graph is built by processing the batch input file and adding a transaction for each new pair of users as a new edge in the graph. When a stream input file is processed, a feature of each transaction is verified, "trusted" or "unverified" written in the output file, and the transaction is added as a graph edge (if new).  

In such a data structure, being in the "friends network" feature of degree n is equivalent to being in the set of a vertex neighbors of degree n. For the challenge feature 1 n is 1, for feature 2 n is 2 and for feature 3 n is 4. 

For features 1 and 2 we can directly look for degree 1 or 2 neighbors without writing special methods. For feature 3 the breadth-first search graph algorithm is implemented. This solution can be used for friends of arbitrary degrees n. The search is stopped after either the payee vertex is visited, after all verteces of degrees less or equal to n are visited, or after all verteces in the graph are visited.

## Feature 4
An additional feature, feature 4, uses date and time of the transaction, as well as the amount of money of the transaction, to keep the track of the total amount of payments received by each user in the current interval of time. When a transaction is processed in real-time it is declared "trusted" if within the curent interval of time the payee received the amount of money that falls within a specified interval. For the purposes of this challenge, the interval of time is one minute (selected to correspond to the interval of time in the given batch_payment.csv file) and the interval of amounts is (100,10000). Similar feature can be developed to monitor the amount paid by each user.  

## Usage
* sh run.sh

or directly 
* python ./src/dwGraph.py batchPaymentFileName streamPaymentFileName output1FileName output2FileName output3FileName output4FileName

For instance,
* python ./src/dwGraph.py ./paymo_input/batch_payment.csv ./paymo_input/stream_payment.csv ./paymo_output/output1.txt ./paymo_output/output2.txt ./paymo_output/output3.txt

## Dependencies
The code uses no special libraries. Only the standard Python packages sys and time are used, but even that is not for essential program features.

## Testing
Tested both in Linux and Windows environments. Due to the LF vs CRLF issues, slight modifications in code needed for the Windows version (commented in the code).

The unit tests are provided in test_dwGraph.py. The command for a batch of unit tests:
*python src/test_dwGraph.py -v

This includes several tests on the long batch_payment.csv input file.

## Performance
On Intel i7 -based laptop at 2.8 GHz the processing of each payment transaction takes on average:
* Feature 1:   7.5 microseconds
* Feature 2:   19.3 microseconds
* Feature 3:   0.3 seconds
