# -*- coding:utf-8 -*-
"""
作者：zhangxl
日期：2020年06月22日
"""
from tkinter import *
from tkinter.ttk import Button
from ch8.person_tax_calc import calc


def calc_count():
    count = countVar.get()
    tax = calc(count)
    labelVar.set("所得税 %.2f 元" % tax)


root = Tk()
root.title("个人所得税计算器 v1.0")
root.geometry('400x200')

topFrame = Frame(root)
Label(topFrame, text='输入月收入:').pack(side=LEFT, padx=5, pady=5)
countVar = IntVar()
Entry(topFrame, textvariable=countVar).pack(side=LEFT, padx=5, pady=5)
Button(topFrame, text="计算", command=calc_count).pack(side=LEFT, padx=5, pady=5)
topFrame.pack()

labelVar = StringVar()
Label(root, textvariable=labelVar, font='微软雅黑 24 normal').pack(pady=20)

root.mainloop()
