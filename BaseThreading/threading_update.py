"""
date: 2021/4/25 13:50
author: leesure
"""
import threading
import time


def doWaiting():
    print(threading.currentThread().getName()+"sub-threading start waiting...")
    time.sleep(5)
    print(threading.currentThread().getName()+"sub-threading end up waiting...")


print("main-threading start running")
for i in range(5):
    t1=threading.Thread(target=doWaiting)
    t1.setDaemon(True)  # setting Daemon is enable to be controlled by main thread.
                        # when main thread finish running, no matter whether Daemon finish running, they must end up running
    t1.start()
# for i in range(10):
#     threading.Thread(target=execute, args=('leeThread' + str(i),)).start()

# t1=threading.Thread(target=doWaiting)
# t1.start()
# print("other operation are executed by main thread")
# t1.join()  # waiting sub-thread that end up execution

print("main-threading end up running")
