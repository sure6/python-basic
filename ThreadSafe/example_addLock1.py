"""
date: 2021/4/25 14:26
author: lee sure
"""
import threading
import time

num = 0
lock = threading.Lock()  # instance the mutex


def add(lk):
    global num
    # add mutex and release mutex together syntax
    # add mutex
    with lk:
        for _ in range(1000000): # If you have fewer loops, cpu can display synchronized execution
            num += 1
        print('sub-thread %s finish running, num = %d' % (threading.currentThread().getName(), num))
    # release mutex

for i in range(2):
    t1 = threading.Thread(target=add, args=(lock,))
    t1.start()
    # t1.join() #  enable to achieve, but belonging to synchronized execution

time.sleep(3)
print('main thread finish running, num = ' + str(num))
