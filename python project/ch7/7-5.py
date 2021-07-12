# -*- coding:utf-8 -*-
"""
作者：zhangxl
日期：2020年06月04日
"""


class Person:
    """类的说明"""
    height = 180  # 类属性 所有实例共享的
    name = '王宝强'

    def __init__(self, name, height):
        # 构造函数
        # 什么是函数？什么是方法？
        # print('i am a Person object')
        self.height = height
        self.name = name

    def say(self):
        print("i am " + self.name)

    @classmethod
    def classSay(cls):
        print("i am " + cls.name)


# person1 = Person('王小蒙', 150)
# person1.say()
#
# person2 = Person('石敢当', 170)
# person2.say()

Person.classSay()
