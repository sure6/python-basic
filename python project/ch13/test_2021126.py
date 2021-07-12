# -*- coding:utf-8 -*-
"""
测试一个ep2 socket请求
作者：zhangxl
日期：2020年11月26日
"""
import socket
import json

serveraddress = ("31.23.45.77", 15004)
# serveraddress = ("localhost", 20019)
# serveraddress = ("localhost", 8888)

sk = socket.socket()

sk.connect(serveraddress)

print("connecting....")

sss = '0000000234{"header":{"serviceCode":"400906","channelTranSeqNo":"1111","description":"","channelType":"0501","channelTranTime":"2020-11-26 10:28:44"},"body":{"id_order":"CCNS20200605102048773404971","service_code":"400906","busichannel":"DSHC"}}'
# sss = '123'

print("发送内容:", sss)

sk.send(sss.encode())

total_len = int(sk.recv(10))
print("报文长度:", total_len)

recv_len = 0
buff_len = 1024
recv_data = b""
while total_len > 0:
    answer = sk.recv(buff_len)
    recv_data += answer
    total_len -= len(answer)

print("收到服务器应答:[%d] %s" % (len(recv_data), recv_data.decode()))

print(json.dumps(json.loads(recv_data.decode('utf-8')), indent=4, ensure_ascii=False))

print(json.loads(recv_data.decode('utf-8')))
sk.shutdown(2)
sk.close()
