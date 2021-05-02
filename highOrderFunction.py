'''
print(abs(-10)) #10
print(abs) #<built-in function abs>
'''
# similar
'''
x=abs(-10)
print(x)
y=abs
print(y)
print(y(-19))
'''
# function name is also a variable
'''
# abs = 10 # error
# abs(-10)
import builtins
# builtins.abs=10
print(builtins.abs)
'''
# 传入函数
# 既然变量可以指向函数，函数的参数能接收变量，那么一个函数就可以接收另一个函数作为参数，这种函数就称之为高阶函数。
'''
def add(a,b,f):
    return f(a)+f(b)

print(add(1, 2, abs))
'''
# map & reduce func
'''
def f(x):
    return x*x

li= map(f, [1,2,3,4,5,6,7,8,9])
li2= map(str, [1,2,3,4,5,6,7,8,9])
print(list(li))
print(list(li2))
'''
from functools import reduce
'''
def fn(x,y):
    return x*10+y

def str2int(s):
    digital = {"0":0,"1":1,"2":2,"3":3,"4":4,"5":5,"6":6,"7":7,"8":8,"9":9}
    return digital[s]

print(list(map(str2int, "13579")))
print(reduce(fn,map(str2int, "13579")))
'''
'''
digtial ={"0":0,"1":1,"2":2,"3":3,"4":4,"5":5,"6":6,"7":7,"8":8,"9":9}
def str2int(s):
    def fn(x,y):
        return x*10+y
    def char2int(s):
        return digtial[s]
    return reduce(fn, map(char2int, s))

print(str2int("13579"))
'''
# excisize
#利用map()函数，把用户输入的不规范的英文名字，变为首字母大写，其他小写的规范名字。输入：['adam', 'LISA', 'barT']，输出：['Adam', 'Lisa', 'Bart']：
# def normalize(name):
#     pass
