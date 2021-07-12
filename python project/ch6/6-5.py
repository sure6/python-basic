# -*- coding:utf-8 -*-
"""
作者：zhangxl
日期：2020年05月28日
"""


def Add(a, b=2):  # 形式参数 和 实际参数
    print("a=", a)
    print("b=", b)
    result = a + b
    return result


c = Add(1)  # 默认值参数
print(c)
