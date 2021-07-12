# -*- coding:utf-8 -*-
"""
作者：zhangxl
日期：2020年06月19日
"""

with open('data_cn.txt', 'w', encoding='utf-8') as file:
    file.write("人生苦短，我用Python")


with open('data_cn.txt', 'r', encoding='utf-8') as file:
    print(file.read())

# encoding的默认值 GBK
with open('data_cn_1.txt', 'r', encoding='utf-8') as file:
    print("cn_1:---------------")
    print(file.read())
