#       TAKEN FROM: CIS 226, Fall 2023
#       This is an example of locks
# -------------------------------------------------------------------------------------------------
"""Locks

Using a Lock means that other threads will have to wait while we access a shared
variable.

This does make the code run slower, but we've gotten rid of the race condition.
"""
import threading

NUM_THREADS = 10
NUM_INCREMENTS = 100000  # 100,000
EXPECTED_TOTAL = NUM_THREADS * NUM_INCREMENTS

lock = threading.Lock()
i = 0


def increment():
    global i
    for x in range(NUM_INCREMENTS):
        with lock:  # Now other threads have to wait. No more race condition
            i += 1


threads = [threading.Thread(target=increment) for _ in range(NUM_THREADS)]
for thread in threads:
    thread.start()

for thread in threads:
    thread.join()

assert i == EXPECTED_TOTAL, 'i was {} instead of {}'.format(i, EXPECTED_TOTAL)
