# -*- coding:utf-8 -*-
"""
作者：zhangxl
日期：2020年06月04日
"""


class Person:
    """类的说明"""
    height = 180  # 类属性 所有实例共享的

    def __init__(self, height):
        # 构造函数
        # 什么是函数？什么是方法？
        print('i am a Person object')
        self.height = height

    def say(self):
        print("i am speaking")
        return 'haha'


person = Person(150)
# person1 = Person()
# person.height = 150
# person1.height = 170
# print(person.say())
print(person.height)
# print(person1.height)
print(Person.height)
print(person.__dict__)
# print(person1.__dict__)
print(Person.__dict__)
