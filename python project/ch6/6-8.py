# -*- coding:utf-8 -*-
"""
作者：zhangxl
日期：2020年05月28日
"""


def print_food(*food, placeno, waiter):
    print("这是第" + placeno + "桌客人的点菜单:")

    for f in food:
        print(f)

    print("服务员:" + waiter)


print_food('宫保鸡丁', '水煮肉片', placeno='12', waiter='小王')
