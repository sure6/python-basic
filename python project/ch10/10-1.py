# -*- coding:utf-8 -*-
"""
作者：zhangxl
日期：2020年06月19日
"""

# 读取的过程 1 打开文件 2 读取文件 3 关闭文件
# r : read
# w : write
# a+ : 读写

# 相对路径 绝对路径
file = open('data.txt', 'r')
# file.seek(6)
# data = file.read(6)
# print(data)

# data = file.readline()
# while data:
#     print(data, end='')
#     data = file.readline()

datas = file.readlines()
print(type(datas))
for line in datas:
    print(line, end='')

file.close()

# with
