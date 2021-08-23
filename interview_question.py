# coding=utf-8
"""
date: 2021/8/23 15:00
author: lee sure
"""
import copy
import json


def any_all():
    a=[1,2,3,4,0]
    b=["a","b","c",""]
    print(any(b))
    print(all(b))

def copy_deepcopy():
    a="haha"
    b=a
    c=copy.copy(a)
    d=copy.deepcopy(a)
    print("b:",id(b))
    print("c:",id(c))
    print("d:",id(d))
    # 改变原来的值, 浅和深拷贝的对象都是不同的地址, 但是改变子对象则浅拷贝也会复制
    list=[1,2,[3,4]]
    list1=copy.copy(list)
    list2=copy.deepcopy(list)
    # list[0]=5
    list[2][0]=5
    print("list:", id(list), list)
    print("list1:", id(list1),list1)
    print("list2:", id(list2),list2)


class demoClass:
    instances_created = 0
    def __new__(cls,*args,**kwargs):
        print("__new__():",cls,args,kwargs)
        instance = super().__new__(cls)
        instance.number = cls.instances_created
        cls.instances_created += 1
        return instance
    def __init__(self,attribute):
        print("__init__():",self,attribute)
        self.attribute = attribute

def list2generator():
    a = [i for i in range(10)]
    print(type(a))
    b = (i for i in range(10))
    print(type(b))

def diff_sort_sorted():
    # 在原list上做修改,无返回值
    list=[0,-1,3,-10,5,9]
    list=["ab","a","abc","abcd"]
        # 按字符长度来排序
    list.sort(key=len,reverse=False)
    print(list)
    # 返回新的list
    list2 = [0, -1, 3, -10, 5, 9]
    res=sorted(list2,reverse=False)
    print(list2)
    print(res)
    #list使用lambda来排序
    list3= [0, -1, 3, -10, 5, 9]
    a=sorted(list3, key=lambda x:x)
    print(a)
    # 正数从小到大,负数从大到小
    list3 = [0, -1, 3, -10, 5, 9,-5]
    b = sorted(list3, key=lambda x: (x<0,abs(x)))
    print(b)
    # 列表里嵌套字典排序
    foo=[{"name":"zhangsan","age":18},{"name":"lisi","age":11},{"name":"wangwu","age":20},{"name":"zhaoliu","age":30}]
    c = sorted(foo, key=lambda x:x["name"], reverse=False)
    d = sorted(foo, key=lambda x:x["age"],reverse=False)
    print(c)
    print(d)
    # 列表里嵌套元组或者列表排序
    foo1=[("zs",17),("ls",6),("ww",16),("zl",20),("jq",20),("wb",20)]
    e=sorted(foo1,key=lambda x:(x[0],x[1]),reverse=False)
    f=sorted(foo1,key=lambda x:(x[1],x[0]),reverse=False)
    print(e)
    print(f)
    # 根据键对字典排序
    foo2={"name":"shuaishuai", "age":19, "city":"Wollongong"}
    # g=zip(foo2.keys(),foo2.values())
    # g=[x for x in g]
    g=[x for x in foo2.items()]
    h=sorted(g,key=lambda x:x[0][0],reverse=False)
    foo3={i[0]:i[1] for i in h }
    print(h)
    print(foo3)

def json2dict():
    dict={"name":"leo", "age":15, "nationality":"Australia"}
    json_str=json.dumps(dict)
    print(type(json_str),json_str)
    str_json='{"name":"leo", "age":15, "nationality":"Australia"}'
    dict2=json.loads(str_json)
    print(type(dict2), dict2)

if __name__=="__main__":
    # any_all()

    # copy_deepcopy()

    # test1 = demoClass("abc")
    # test2 = demoClass("xyz")
    # print(test1.number, test1.instances_created)
    # print(test2.number, test2.instances_created)

    # list2generator()

    # diff_sort_sorted()

    json2dict()