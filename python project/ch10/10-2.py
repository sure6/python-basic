# -*- coding:utf-8 -*-
"""
作者：zhangxl
日期：2020年06月19日
"""

# file = open('data.txt', 'r')
with open('data.txt', 'r') as file:
    datas = file.readlines()
    print(type(datas))
    for line in datas:
        print(line, end='')

# file.close()
