#       TAKEN FROM: CIS 226, Fall 2023
#       This is an example of a race condition
# -------------------------------------------------------------------------------------------------
"""Race Condition Example
Adapted from https://stackoverflow.com/questions/1717393/is-the-operator-thread-safe-in-python

If you run this a couple times, you will probably get an error like the
following:

Traceback (most recent call last):
  File "ex02_race_condition.py", line 22, in <module>
    assert i == EXPECTED_TOTAL, 'i was {} instead of {}'.format(i, EXPECTED_TOTAL)
AssertionError: i was 809520 instead of 1000000
"""
import threading

NUM_THREADS = 10
NUM_INCREMENTS = 100000  # 100,000
EXPECTED_TOTAL = NUM_THREADS * NUM_INCREMENTS

i = 0


def increment():
    global i
    for i in range(NUM_INCREMENTS):
        i += 1  # This is not atomic! Vulnerable to race condition


threads = [threading.Thread(target=increment) for _ in range(NUM_THREADS)]
for thread in threads:
    thread.start()

for thread in threads:
    thread.join()

assert i == EXPECTED_TOTAL, 'i was {} instead of {}'.format(i, EXPECTED_TOTAL)
