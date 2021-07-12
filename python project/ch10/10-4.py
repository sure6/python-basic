# -*- coding:utf-8 -*-
"""
作者：zhangxl
日期：2020年06月19日
"""

# 文件的写入

with open('data_write.txt', 'a') as file:
    # data = 'hello python'
    # file.write(data+'\n')
    # data = 'i am sniper'
    # file.write(data)

    datas = ['hello python', 'i am sniper', 'like']

    # for data in datas:
    #     file.write(data+'\n')

    file.writelines([data+'\n' for data in datas])
    # file.writelines("\n".join(datas))
    # file.write("\n".join(datas))
