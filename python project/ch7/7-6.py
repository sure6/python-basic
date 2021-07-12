# -*- coding:utf-8 -*-
"""
作者：zhangxl
日期：2020年06月04日
"""


class Person:
    """类的说明"""
    count = 0

    def __init__(self, name, height):
        # 构造函数
        self.__height = height
        self.name = name
        __class__.count += 1
        print('我是第' + str(__class__.count) + "实例，我叫"+self.name)

    def __say(self):
        print("i am " + self.name)

    @property
    def height(self):
        # 可以做一些检查，权限校验
        return self.__height

    def getHeight(self):
        # 可以做一些检查，权限校验
        return self.__height

    def setHeight(self, height):
        # 检查一下，入口参数的合法性
        self.__height = height

    @classmethod
    def classCount(cls):
        print("一共实例化了" + str(cls.count) + "个Person对象.")


person = Person('王小蒙', 150)

print(person)  # 我是王小蒙 我身高150cm
# print("我是"+person.name + " 我身高" + str(person.height) + "cm")

