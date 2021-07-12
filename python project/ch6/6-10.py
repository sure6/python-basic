# -*- coding:utf-8 -*-
"""
作者：zhangxl
日期：2020年05月28日
"""

# 变量的作用域

a = 'abc'  # 全局变量


def test():
    global a
    a = 'def'  # 局部变量
    print('函数内部的a', a)


print('调用前的a:', a)
test()
print('调用后的a:', a)
