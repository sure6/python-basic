# -*- coding:utf-8 -*-
"""
作者：zhangxl
日期：2020年06月04日
"""


class Person:
    """类的说明"""
    def __init__(self):
        # 构造函数
        # 什么是函数？什么是方法？
        print('i am a Person object')

    def say(self):
        print("i am speaking")
        return 'haha'


person = Person()
print(person.say())
