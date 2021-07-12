# -*- coding:utf-8 -*-
"""
mysql
作者：zhangxl
日期：2020年06月20日
"""

# 1连接数据库 2 拿到游标 3 执行sql 4 关闭游标 5关闭数据库的连接

import pymysql

# 连接
conn = pymysql.connect('localhost', 'root', 'root', 'testdb')

# 拿到游标
cursor = conn.cursor()

# 执行sql
sql = "create table user (id int(11) primary key, name varchar(50))"
cursor.execute(sql)

# 关闭游标和连接
cursor.close()
conn.close()
