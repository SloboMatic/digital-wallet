#!/usr/bin/env bash

# main run on complete bath_payment file and complete stream file
#python ./src/dwGraph.py ./paymo_input/batch_payment.csv ./paymo_input/stream_payment.csv ./paymo_output/output1.txt ./paymo_output/output2.txt ./paymo_output/output3.txt ./paymo_output/output4.txt

# test in SM-test on complete bath_payment file and 20 streaming transactions
#python ./src/dwGraph.py ./insight_testsuite/tests/SM-test/paymo_input/batch_payment.csv ./insight_testsuite/tests/SM-test/paymo_input/stream_payment.csv ./paymo_output/output1.txt ./paymo_output/output2.txt ./paymo_output/output3.txt ./paymo_output/output4.txt

# test in test-1-paymo-trans with 1 streaming transaction
python ./src/dwGraph.py ./insight_testsuite/tests/test-1-paymo-trans/paymo_input/batch_payment.txt ./insight_testsuite/tests/test-1-paymo-trans/paymo_input/stream_payment.txt ./paymo_output/output1.txt ./paymo_output/output2.txt ./paymo_output/output3.txt ./paymo_output/output4.txt

