# -*- coding:utf-8 -*-
"""
date: 2021/4/24 19:36
author: leesure
"""
import socketserver


class MyHandler(socketserver.BaseRequestHandler):
    def handle(self):
        while True:
            data = self.request.recv(1024).decode()
            if data == "exit" or data == "":
                # print("ending...")
                print("client %s: %s has finish sending, closing connection." % self.client_address)
                break
            print("receive info from client that %s send: %s" % (self.client_address, data))
            res = data.upper()
            self.request.sendall(res.encode())
        self.request.close()


hostAddress = ("127.0.0.1", 8888)
sever = socketserver.ThreadingTCPServer(hostAddress, MyHandler)
print("start socketserver, wait to connect client...")
sever.serve_forever()
