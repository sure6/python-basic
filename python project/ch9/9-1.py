# -*- coding:utf-8 -*-
"""
作者：zhangxl
日期：2020年06月18日
"""
from ch9.TranError import TranError
# print(10 / 0)

try:
    #
    # print(10 / 0)
    # a = b + 1
    a = 1 + 1
    b = 3 * 2

    a = int('abc')

    # raise TranError(500001, 'tranError')
except (NameError, ZeroDivisionError) as e:
    print(type(e))
    print(e)
except Exception as e:
    print(e)
    print(type(e))
else:
    print("else")
finally:
    print('finally')

print('2')
