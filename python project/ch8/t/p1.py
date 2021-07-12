# -*- coding:utf-8 -*-
"""
作者：zhangxl
日期：2020年06月13日
"""

__all__ = ['a', 'b', 'Kid', 'Add']

a = 1
b = 2


def Add(x, y):
    return x + y


class Kid:
    def __init__(self, age):
        self.age = age

    def laugh(self):
        print('我%d岁了.' % self.age)


if __name__ == '__main__':
    print(Add(4, 5))
