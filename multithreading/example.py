#       TAKEN FROM: CIS 226, Fall 2023
#       This is an example of threading
# -------------------------------------------------------------------------------------------------
"""Threading Example

--- Sequential ---
START 1
STOP 1
START 2
STOP 2
--- Threaded ---
START 1
START 2
STOP 1
STOP 2

Notice in Threaded, both tasks start and then both finish.
"""

import time
import threading


def do_thing(task_id):
    # Simulate a task
    print("START", task_id)
    # Work goes here...
    time.sleep(1)
    print("STOP", task_id)


def run_sequentially():
    print('--- Sequential ---')
    do_thing(1)
    do_thing(2)


def run_threaded():
    # Create a thread for each
    # (2,) is a tuple of length 1. The comma is important.
    # Notice it's target=do_thing and not target=do_thing()
    t1 = threading.Thread(target=do_thing, args=(1,))
    t2 = threading.Thread(target=do_thing, args=(2,))

    print('--- Threaded ---')
    t1.start()
    t2.start()

    # Wait for our threads to finish (this is blocking)
    # Without this the program would quit before the threads finished
    t1.join()
    t2.join()


if __name__ == '__main__':
    run_sequentially()
    run_threaded()
