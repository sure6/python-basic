# -*- coding:utf-8 -*-
"""
作者：zhangxl
日期：2020年07月01日
"""
import socket

serveraddress = ("127.0.0.1", 8888)

sk = socket.socket()

sk.connect(serveraddress)

while True:
    sss = input('发送内容:').strip()

    sk.sendall(sss.encode())

    if sss == 'exit':
        print('客户端退出连接.')
        break

    answer = sk.recv(1024).decode()

    print("收到服务器应答: %s" % answer)

sk.close()
