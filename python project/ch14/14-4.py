# -*- coding:utf-8 -*-
"""
作者：zhangxl
日期：2020年07月01日
"""
import threading
import time


def dowaiting():
    print(threading.current_thread().getName() + '子线程开始等待...')
    time.sleep(3)
    print(threading.current_thread().getName() + '子线程等待结束')


print('主线程开始')
for i in range(3):
    t = threading.Thread(target=dowaiting)
    t.setDaemon(True)
    t.start()

print('主线程结束')
