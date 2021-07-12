# -*- coding:utf-8 -*-
"""
作者：zhangxl
日期：2020年06月04日
"""
from ch7.p1 import Person


class Worker(Person):
    """这是工人类"""
    def __init__(self, name, height, factory):
        super().__init__(name, height)
        self.factory = factory

    def work(self):
        print("我是"+self.name+"我在"+self.factory+"工作.")

    def say(self):
        print(self.name + "是一名工人，在说话.")
