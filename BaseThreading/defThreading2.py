"""
date: 2021/4/25 13:44
author: leesure
"""
import threading


def execute(name):
    print("threading %s start..." % name)


for i in range(10):
    threading.Thread(target=execute, args=('leeThread' + str(i),)).start()
