"""
date: 2021/4/24 16:30
author: leesure
"""
import socket

serverAddress = ("127.0.0.1", 8888)

sk = socket.socket()

sk.connect(serverAddress)

while True:

    sss = input("sending content:").strip()

    sk.sendall(sss.encode())
    if sss == "exit":
        print("quit connection...")
        break

    answer = sk.recv(1024).decode()

    print("receive answer from server: %s " % answer)

sk.close()
