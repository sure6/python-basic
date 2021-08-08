"""
date: 2021/4/25 13:31
author: leesure
"""
import threading


class MyThread(threading.Thread):
    def __init__(self, thread_name):
        super(MyThread, self).__init__(name=thread_name)

    def run(self):
        print("threading %s start..." % self.name)


for i in range(10):
    MyThread('leeThread' + str(i)).start()
