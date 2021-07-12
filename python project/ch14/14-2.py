# -*- coding:utf-8 -*-
"""
作者：zhangxl
日期：2020年07月01日
"""
import threading


def show(num):
    print('当前线程: %d 在执行...' % num)


for i in range(10):
    t = threading.Thread(target=show, args=(i,))
    t.start()
