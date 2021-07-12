# -*- coding:utf-8 -*-
"""
作者：zhangxl
日期：2020年06月19日
"""

from ch10.appConfig import configData

print("数据库地址:", configData['db_url'])
print("数据库端口:", configData['db_port'])
print("数据库用户:", configData['db_user'])
print("数据库密码:", configData['db_pass'])
