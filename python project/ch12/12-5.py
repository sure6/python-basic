# -*- coding:utf-8 -*-
"""
作者：zhangxl
日期：2020年06月22日
"""
# 标签 Label
from tkinter import *
from tkinter import messagebox


def login():
    username = userVar.get()
    password = passVar.get()
    if username == '' or password == '':
        messagebox.showinfo('错误', '用户名和密码不能为空.')
    elif username == 'sniper' and password == '123456':
        messagebox.showinfo('信息', '登录成功.')
    else:
        messagebox.showinfo('错误', '用户名和密码不匹配.')


root = Tk()
root.title("模拟登录")
root.geometry("400x200+400+300")

Label(root, text='请输入用户名和密码:').pack(pady=20)

userFrame = Frame(root)
Label(userFrame, text='用户名:').pack(side=LEFT, padx=5, pady=5)
userVar = StringVar()
Entry(userFrame, textvariable=userVar).pack(side=LEFT, padx=5, pady=5)
userFrame.pack()

passFrame = Frame(root)
Label(passFrame, text='密   码:').pack(side=LEFT, padx=5, pady=5)
passVar = StringVar()
Entry(passFrame, textvariable=passVar, show="*").pack(side=LEFT, padx=5, pady=5)
passFrame.pack()

buttonFrame = Frame(root)
Button(buttonFrame, text='登录', command=login).pack(side=LEFT, padx=5, pady=5)
Button(buttonFrame, text='取消', command=root.destroy).pack(side=LEFT, padx=5, pady=5)
buttonFrame.pack()

root.mainloop()
