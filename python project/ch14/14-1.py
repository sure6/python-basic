# -*- coding:utf-8 -*-
"""
多线程编程创建方式
作者：zhangxl
日期：2020年07月01日
"""
import threading


# 第一种 继承Thread
class MyThread(threading.Thread):
    def __init__(self, thread_name):
        super(MyThread, self).__init__(name=thread_name)

    def run(self):
        print("%s 在执行中..." % self.name)


for i in range(10):
    MyThread("testThread" + str(i)).start()
