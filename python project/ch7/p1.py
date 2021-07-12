# -*- coding:utf-8 -*-
"""
作者：zhangxl
日期：2020年06月04日
"""


class Person:
    """这是人类，是学生和工人的父类，人类有名字和身高，可以跑步和说话"""

    def __init__(self, name, height):
        self.name = name
        self.height = height

    def run(self):
        print(self.name + "在跑步.")

    def say(self):
        print(self.name + "在说话.")
