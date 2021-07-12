# -*- coding:utf-8 -*-
"""
作者：zhangxl
日期：2020年07月01日
"""
import socket

hostaddress = ("127.0.0.1", 8888)

# 使用ipv4 使用TCP协议
sk = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
sk.bind(hostaddress)
sk.listen(5)
print("启动socket服务，等待客户端连接...")

conn, clientaddress = sk.accept()

while True:
    # bytes
    data = conn.recv(1024).decode()

    if data == 'exit':
        print("客户端发送完成，断开连接.")
        break

    print("接收到客户端 %s 发送来的信息 : %s" % (clientaddress, data))

    res = data.upper()

    # str
    conn.sendall(res.encode())

conn.close()
