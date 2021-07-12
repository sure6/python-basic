# -*- coding:utf-8 -*-
"""
作者：zhangxl
日期：2020年05月28日
"""


# 可变参数 一个*表示是一个序列类型的的可变参数
# **代表是一个字典类型的可变参数
def test(*value):
    print(type(value))
    for v in value:
        print(v)


test('hello', 'world', 'python')
