#!/usr/bin/env bash
#python ./src/dwGraph.py ./paymo_input/batch_payment.csv ./paymo_input/stream_payment.csv ./paymo_output/output1.txt ./paymo_output/output2.txt ./paymo_output/output3.txt
#python ./src/dwGraph.py ./paymo_input/batch_payment.csv ./paymo_input/stream_test_20.csv ./paymo_output/output1.txt ./paymo_output/output2.txt ./paymo_output/output3.txt
python ./src/dwGraph.py ./insight_testsuite/tests/test-1-paymo-trans/paymo_input/batch_payment.txt ./insight_testsuite/tests/test-1-paymo-trans/paymo_input/stream_payment.txt ./paymo_output/output1.txt ./paymo_output/output2.txt ./paymo_output/output3.txt

