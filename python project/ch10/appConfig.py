# -*- coding:utf-8 -*-
"""
作者：zhangxl
日期：2020年06月19日
"""

configData = {}
with open('app.config', 'r') as file:
    datas = file.readlines()
    for line in datas:
        if line.startswith("#"):
            continue
        key = line.split("=")[0]
        value = line.split("=")[1].replace("\n", "")
        configData[key] = value

if __name__ == '__main__':
    print(configData)
