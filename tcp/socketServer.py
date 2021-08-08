"""
date: 2021/4/24 16:31
author: leesure
"""
import socket

hostAddress = ("127.0.0.1", 8888)
sk = socket.socket(socket.AF_INET)
sk.bind(hostAddress)
sk.listen(5)
print("start socketserver, wait to connect client...")

conn, ipaddress = sk.accept()
while True:

    data = conn.recv(1024).decode()
    if data == "exit":
        print("client has finish sending, closing connection.")
        break

    print("receive info from client that %s send: %s" % (ipaddress, data))

    res = data.upper()

    conn.sendall(res.encode())

conn.close()