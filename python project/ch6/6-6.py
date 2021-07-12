# -*- coding:utf-8 -*-
"""
作者：zhangxl
日期：2020年05月28日
"""


def print_userinfo(name, gender='男', age=23, depart='中国一汽'):
    print("我是"+name)
    print("我是"+gender+"生")
    print("我今年"+str(age)+"岁")
    print("我在"+depart+"工作")


print_userinfo('小华', '男', 23, '长春一汽')
print("="*10)
print_userinfo('小华')
print("="*10)
print_userinfo('小华', age=30, depart='欧亚商都')
print("="*10)
print_userinfo('小华', depart='欧亚商都', age=30)
print("="*10)
print_userinfo('小华')
