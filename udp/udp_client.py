"""
date: 2021/4/24 22:42
author: leesure
"""
import socket

serverAddress = ("127.0.0.1", 9999)

sk = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

while True:
    sss=input("[UDP]sending content:").strip()
    sk.sendto(sss.encode(), serverAddress)
    if sss=='exit':
        print('client quit...')
        break
sk.close()