# -*- coding:utf-8 -*-
"""
作者：zhangxl
日期：2020年06月18日
"""


class TranError(Exception):
    def __init__(self, errorCode=500000, message='tranError'):
        self.errorCode = errorCode
        self.message = message

    def __str__(self):
        return "[%d] %s" % (self.errorCode, self.message)
