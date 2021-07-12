# -*- coding:utf-8 -*-
"""
作者：zhangxl
日期：2020年07月01日
"""
import socket

hostaddress = ("127.0.0.1", 9999)

sk = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
sk.bind(hostaddress)
print("启动udp socket服务，等待客户端数据...")

while True:
    data = sk.recv(1024).decode()
    print("udp服务器接收到客户端的数据: %s" % data)
    if data == 'exit':
        print("客户端请求退出.")
        break

sk.close()
