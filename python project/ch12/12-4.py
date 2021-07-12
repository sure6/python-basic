# -*- coding:utf-8 -*-
"""
作者：zhangxl
日期：2020年06月22日
"""
# 标签 Label
from tkinter import *
from ch12.person_tax_calc import calc


def tax_calc():
    inputCount = inputVar.get()
    tax = calc(int(inputCount))
    outputVar.set("所得税: %.2f 元" % tax)


root = Tk()
root.title("个人所得税计算器 v1.0")
root.geometry("400x200+400+300")

topFrame = Frame(root)
inputLabel = Label(topFrame, text='请输入月收入:')
inputLabel.pack(side=LEFT, padx=5, pady=5)

inputVar = StringVar()
inputEntry = Entry(topFrame, textvariable=inputVar)
inputEntry.pack(side=LEFT, )

inputButton = Button(topFrame, text='计算', command=tax_calc)
inputButton.pack(side=LEFT, padx=5, pady=5)
topFrame.pack(padx=5, pady=5)

outputVar = StringVar()
outputVar.set('点击计算')
outputLabel = Label(root, textvariable=outputVar, font='微软雅黑 24 normal', fg='green')
outputLabel.pack(padx=5, pady=5)

root.mainloop()

# 布局相关的方法 pack() grid() place()
