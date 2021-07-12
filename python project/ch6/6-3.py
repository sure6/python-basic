# -*- coding:utf-8 -*-
"""
作者：zhangxl
日期：2020年05月28日
"""


def Add_Sub(a, b):
    sum = a + b
    sub = a - b
    return sum, sub


# c = Add_Sub(4, 1)
# print(type(c))
# print(c)
# print(c[0], c[1])

sum, sub = Add_Sub(4, 1)
print(sum, sub)
