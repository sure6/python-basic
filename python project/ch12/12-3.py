# -*- coding:utf-8 -*-
"""
作者：zhangxl
日期：2020年06月22日
"""
# 标签 Label
from tkinter import *

root = Tk()
root.title("个人所得税计算器 v1.0")
root.geometry("400x200+400+300")

inputLabel = Label(root, text='人生苦短，我用Python', bg='lightblue', font='微软雅黑 12 normal')
inputLabel.pack(padx=5, pady=10, fill=X)

inputLabel = Label(root, text='人生苦短，我用Python', bg='lightyellow', font='微软雅黑 12 normal')
inputLabel.pack(padx=5, pady=10, fill=BOTH, expand=True)


root.mainloop()
