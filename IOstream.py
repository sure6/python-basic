# y=open("D:\\leesure.txt","w")
# y.write("leesure is so handsome\n啊大啊大苏打")
# y.close()

# f=open("D:\\leesure.txt","rb+")
# content = f.tell()
# print(content)
# f.close()

# y=open("D:\\leesure.txt","a")
# word_num= y.write("leesure is so handsome\n啊大啊大苏打")
# print(word_num)
# y.close()

# print(b'0123456789abcdef') # b->binary/byte r/R-> removes the backslash transfer mechanism u->unicode 以 f开头表示在字符串内支持大括号内的python 表达式

#Stringio and Bytesio
# from io import StringIO #  import StringiO from module
'''
# f=StringIO()
# num=f.write("Hello python IO")
# print(num)
# print(f.getvalue())
'''
'''
f=StringIO("helloIO\nHiIO\ngoodbyeIO")
while True:
    s=f.readline()
    if s=="":
        break
    print(s.strip())
'''
'''
from io import BytesIO #  import ByteIO from module
f=BytesIO()
num= f.write("中国".encode("utf-8"))
print(num)
print(f.getvalue())
'''

# operate content and file
'''
# import os
# import os.path
# import stat
# import time
# print(os.name)
# print(os.path.abspath(".")) # "." 代表当前路径 基于linux and windows
# current_path = os.path.abspath(".")
# statinfo = os.stat(current_path)
# print(type(statinfo))
# mode = statinfo.st_mode
# print(mode)
# time.strftime("%b %d %H:%M",time.localtime(statinfo.st_mtime))
'''

# list all files in current document 
# print([x for x in os.listdir('.') if os.path.isfile(x) and os.path.splitext(x)[1]==".py"])

# pickling (like serialization) 序列化
import pickle
'''
# Python内置的json模块提供了非常完善的Python对象到JSON格式的转换。我们先看看如何把Python对象变成一个JSON：

d=dict(name="leesure", age=26, score=99)
print(pickle.dumps(d))

with open("D:\\sure.txt","rb") as f:
# pickle.dump(d, f)

    d= pickle.load(f)  
print(d)
print(type(d))
'''
'''
import json
d=dict(name="leesure", age=26, score=99)
print(json.dumps(d))
'''

""" import json
class Student(object):
    def __init__(self, name, age, score):
        self.name=name
        self.age=age
        self.score=score
 
# def student2dict(std):
#     return {'name':std.name,'age':std.age,'score':std.score} 
s = Student("Bob", 20, 88)
print(json.dumps(s,default=lambda s:s.__dict__))
# print(dir(s)) """