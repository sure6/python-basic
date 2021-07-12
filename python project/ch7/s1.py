# -*- coding:utf-8 -*-
"""
作者：zhangxl
日期：2020年06月04日
"""
from ch7.p1 import Person


class Student(Person):
    def __init__(self, name, height, stno, school):
        super().__init__(name, height)
        self.stno = stno
        self.school = school

    def do_homework(self):
        print("我是"+self.name+"我在"+self.school+"上学，我在写作业!")
