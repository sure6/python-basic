# -*- coding:utf-8 -*-
"""
作者：zhangxl
日期：2020年07月01日
"""
import socket
import threading


def deal(link, client):
    print('新线程开始处理客户端 %s: %s 的数据请求' % client)
    while True:
        # bytes
        data = link.recv(1024).decode()
        if data == 'exit':
            print("客户端发送完成，断开连接.")
            break
        print("接收到客户端 %s 发送来的信息 : %s" % (client, data))
        # res = data.upper()
        res = data * 1000
        # str
        link.sendall(res.encode())
    link.close()


hostaddress = ("127.0.0.1", 8888)

# 使用ipv4 使用TCP协议
sk = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
sk.bind(hostaddress)
sk.listen(5)
print("启动socket服务，等待客户端连接...")

while True:
    conn, clientaddress = sk.accept()
    xd = threading.Thread(target=deal, args=(conn, clientaddress))
    xd.start()
