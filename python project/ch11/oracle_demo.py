# -*- coding:utf-8 -*-
"""
作者：zhangxl
日期：2020年06月20日
"""

# cx_Oracle 和 PyMySql一样是支持Oracle连接API 模块
# 首先要用pip install cx_Oracle来安装
import cx_Oracle as orcl

# 连接方法和参数与PyMySql稍有不同，但是原理都是一样的
conn = orcl.connect('ep2eas/ep2eas@31.23.40.14:1521/CCBDEV')
cursor = conn.cursor()
try:
    # 一下代码为查询多条数据的例子
    """
    cursor.execute("select * from userinfo")  # execute方法返回值不是数据条数了，要注意和MySql的区别
    rows = cursor.fetchall()
    print("共查询到%d条数据:" % len(rows))  # Oracle获取条数方法与MySql不同
    for row in rows:
        print(row)
    """

    # 查询一条数据
    cursor.execute("select * from userinfo where usercode='800406'")
    row = cursor.fetchone()
    print(row)
except Exception as e:
    print("查询出错：", e)
finally:
    # 不要忘记关闭游标和数据库连接
    cursor.close()
    conn.close()
