"""
date: 2021/4/27 14:06
author: lee sure
"""

with open("C:\\python-workspace\\pyFileIO\\demo.txt", 'r') as f:
    # f.seek(0,2)
    # print(f.tell())
    # f.write("fgh".encode())
    # f.write("asa".encode())
    for i in f:
        print(i.rstrip())

    # f.write("hello, python")
    # f.seek()

