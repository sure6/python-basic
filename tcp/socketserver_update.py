"""
date: 2021/4/24 16:31
author: leesure
"""
import socket
import threading


def cope_with(connection, client):
    print("new thread will start to cope with request from client %s: %s " % client)
    while True:
        data = conn.recv(2048).decode()
        if data == "exit" or data=="":
            # print("ending...")
            print("client %s: %s has finish sending, closing connection." % client)
            break
        print("receive info from client that %s: %s send: %s" % (client[0], client[1], data))
        res = data.upper()
        connection.sendall(res.encode())

    connection.close()


hostAddress = ("127.0.0.1", 8888)
sk = socket.socket(socket.AF_INET)
sk.bind(hostAddress)
sk.listen(10)
print("start socketserver, wait to connect client...")
while True:
    conn, ipaddress = sk.accept()
    # print(conn, ipaddress)
    t = threading.Thread(target=cope_with, args=(conn, ipaddress))
    t.start()
