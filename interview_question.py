# coding=utf-8
"""
date: 2021/8/23 15:00
author: lee sure
"""
import copy
import functools
import json


def any_all():
    a = [1, 2, 3, 4, 0]
    b = ["a", "b", "c", ""]
    print(any(b))
    print(all(b))


def copy_deepcopy():
    a = "haha"
    b = a
    c = copy.copy(a)
    d = copy.deepcopy(a)
    print("b:", id(b))
    print("c:", id(c))
    print("d:", id(d))
    # 改变原来的值, 浅和深拷贝的对象都是不同的地址, 但是改变子对象则浅拷贝也会复制
    list = [1, 2, [3, 4]]
    list1 = copy.copy(list)
    list2 = copy.deepcopy(list)
    # list[0]=5
    list[2][0] = 5
    print("list:", id(list), list)
    print("list1:", id(list1), list1)
    print("list2:", id(list2), list2)


class demoClass:
    instances_created = 0

    def __new__(cls, *args, **kwargs):
        print("__new__():", cls, args, kwargs)
        instance = super().__new__(cls)
        instance.number = cls.instances_created
        cls.instances_created += 1
        return instance

    def __init__(self, attribute):
        print("__init__():", self, attribute)
        self.attribute = attribute


def list2generator():
    a = [i for i in range(10)]
    print(type(a))
    b = (i for i in range(10))
    print(type(b))


def diff_sort_sorted():
    # 在原list上做修改,无返回值
    list = [0, -1, 3, -10, 5, 9]
    list = ["ab", "a", "abc", "abcd"]
    # 按字符长度来排序
    list.sort(key=len, reverse=False)
    print(list)
    # 返回新的list
    list2 = [0, -1, 3, -10, 5, 9]
    res = sorted(list2, reverse=False)
    print(list2)
    print(res)
    # list使用lambda来排序
    list3 = [0, -1, 3, -10, 5, 9]
    a = sorted(list3, key=lambda x: x)
    print(a)
    # 正数从小到大,负数从大到小
    list3 = [0, -1, 3, -10, 5, 9, -5]
    b = sorted(list3, key=lambda x: (x < 0, abs(x)))
    print(b)
    # 列表里嵌套字典排序
    foo = [{"name": "zhangsan", "age": 18}, {"name": "lisi", "age": 11}, {"name": "wangwu", "age": 20},
           {"name": "zhaoliu", "age": 30}]
    c = sorted(foo, key=lambda x: x["name"], reverse=False)
    d = sorted(foo, key=lambda x: x["age"], reverse=False)
    print(c)
    print(d)
    # 列表里嵌套元组或者列表排序
    foo1 = [("zs", 17), ("ls", 6), ("ww", 16), ("zl", 20), ("jq", 20), ("wb", 20)]
    e = sorted(foo1, key=lambda x: (x[0], x[1]), reverse=False)
    f = sorted(foo1, key=lambda x: (x[1], x[0]), reverse=False)
    print(e)
    print(f)
    # 根据键对字典排序
    foo2 = {"name": "shuaishuai", "age": 19, "city": "Wollongong"}
    # g=zip(foo2.keys(),foo2.values())
    # g=[x for x in g]
    g = [x for x in foo2.items()]
    h = sorted(g, key=lambda x: x[0][0], reverse=False)
    foo3 = {i[0]: i[1] for i in h}
    print(h)
    print(foo3)


def json2dict():
    dict = {"name": "leo", "age": 15, "nationality": "Australia"}
    json_str = json.dumps(dict)
    print(type(json_str), json_str)
    str_json = '{"name":"leo", "age":15, "nationality":"Australia"}'
    dict2 = json.loads(str_json)
    print(type(dict2), dict2)


def func_program():
    # map() 函数的功能是对可迭代对象中的每个元素，都调用指定的函数，并返回一个 map 对象。
    list1 = [1, 2, 3, 4, 5]
    list2 = [3, 4, 5, 6, 7]
    a = map(lambda x, y: x + y, list1, list2)
    b = [i for i in a]
    print(b)
    # filter() 函数的功能是对 iterable 中的每个元素，都使用 function 函数判断，并返回 True 或者 False，最后将返回 True 的元素组成一个新的可遍历的集合。
    c = filter(lambda x: x % 2 == 0, list1)
    c = [i for i in c]
    print(c)

    new_list = map(lambda x, y: x - y > 0, [3, 5, 6], [1, 5, 8])
    print(list(new_list))

    # reduce() 函数通常用来对一个集合做一些累积操作
    reduce = functools.reduce(lambda x, y: x * y, list1)
    print(reduce)


u = "external variable"


def variable_scope(p):
    # 注意，在使用 global 关键字修饰变量名时，不能直接给变量赋初值，否则会引发语法错误。global无法对参数进行修饰
    global t
    t = "interner variable"
    # globals() 函数为 Python 的内置函数，它可以返回一个包含全局范围内所有变量的字典，该字典中的每个键值对，键为变量名，值为该变量的值。
    print(globals())
    # 一个包含当前作用域内所有变量的字典。这里所谓的“当前作用域”指的是，在函数内部调用 locals() 函数，会获得包含所有局部变量的字典；而在全局范文内调用 locals() 函数，其功能和 globals() 函数相同。
    print(locals())
    print(t, u, p)
    #  vars() 函数也是 Python 内置函数，其功能是返回一个指定 object 对象范围内所有变量组成的字典。如果不传入object 参数，vars() 和 locals() 的作用完全相同。


def closure_external(exponent):
    """
    闭包，又称闭包函数或者闭合函数，其实和前面讲的嵌套函数类似，不同之处在于，闭包中外部函数返回的不是一个具体的值，而是一个函数。一般情况下，返回的函数会赋值给一个变量，这个变量可以在后面被继续执行调用。
    :param exponent:
    :return:
    """
    def closure_internal(number):
        return number ** exponent

    return closure_internal


if __name__ == "__main__":
    # any_all()

    # copy_deepcopy()

    # test1 = demoClass("abc")
    # test2 = demoClass("xyz")
    # print(test1.number, test1.instances_created)
    # print(test2.number, test2.instances_created)

    # list2generator()

    # diff_sort_sorted()

    # json2dict()

    # func_program()

    # variable_scope("parameters")
    # print(u)
    # # print(p)
    # print(t)
    # print(globals())

    a = closure_external(3)
    b = a(5)
    print(b)
    # 该属性记录着自由变量的地址
    print(a.__closure__)
