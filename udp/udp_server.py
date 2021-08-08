"""
date: 2021/4/24 22:34
author: leesure
"""
import socket

hostAddress = ("127.0.0.1", 9999)
sk = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
sk.bind(hostAddress)
print("start udp_socket server, waiting for client's data...")
while True:
    data = sk.recv(1024).decode()
    print('udp server receive data from client: %s ' % data)
    if data == "exit":
        print('client request quitting...')
        break

sk.close()