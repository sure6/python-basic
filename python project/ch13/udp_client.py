# -*- coding:utf-8 -*-
"""
作者：zhangxl
日期：2020年07月01日
"""
import socket

serveraddress = ("127.0.0.1", 9999)
sk = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

while True:
    sss = input('[UDP]发送内容:').strip()
    sk.sendto(sss.encode(), serveraddress)
    if sss == 'exit':
        print('客户端退出.')
        break

sk.close()
