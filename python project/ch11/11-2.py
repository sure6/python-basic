# -*- coding:utf-8 -*-
"""
sqlite
作者：zhangxl
日期：2020年06月20日
"""

# 1连接数据库 2 拿到游标 3 执行sql 4 关闭游标 5关闭数据库的连接

import sqlite3

# 连接
conn = sqlite3.connect('test.db')

# 拿到游标
cursor = conn.cursor()

# 执行sql
sql = "insert into user (id,name) values ('2', '张无忌')"
cursor.execute(sql)
sql = "insert into user (id,name) values ('3', '令狐冲')"
cursor.execute(sql)
sql = "insert into user (id,name) values ('4', '任盈盈')"
cursor.execute(sql)

# 关闭游标和连接
cursor.close()

conn.commit()
conn.close()
