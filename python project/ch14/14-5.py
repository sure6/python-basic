# -*- coding:utf-8 -*-
"""
线程安全
作者：zhangxl
日期：2020年07月01日
"""
import threading
import time
number = 0

# 1 : 1000
# 2 : 2000
# 1 : 2120
# 2 : 3456


def add():
    global number
    for _ in range(1000000):
        number += 1
    print('子线程 %s 执行结束后：number = %d' % (threading.current_thread().getName(), number))


for i in range(2):
    t = threading.Thread(target=add)
    t.start()

time.sleep(3)
print('主线程结束，number = '+str(number))
