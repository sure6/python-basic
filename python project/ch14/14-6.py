# -*- coding:utf-8 -*-
"""
线程安全
作者：zhangxl
日期：2020年07月01日
"""
import threading
import time
number = 0
lock = threading.Lock()


def add(lk):
    global number
    # 加锁
    with lk:
        for _ in range(1000000):
            number += 1
        print('子线程 %s 执行结束后：number = %d' % (threading.current_thread().getName(), number))
        # 解锁


for i in range(2):
    t = threading.Thread(target=add, args=(lock,))
    t.start()

time.sleep(3)
print('主线程结束，number = '+str(number))
