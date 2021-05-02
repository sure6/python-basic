#Python 中的变量不需要声明。每个变量在使用前都必须赋值，变量赋值以后该变量才会被创建。
#在 Python 中，变量就是变量，它没有类型，我们所说的"类型"是变量所指的内存中对象的类型。 
#Python3 中有六个标准的数据类型：number(float,integer and complex) String List tuple set dictionary
#number(float and integer) String  tuple 属于数据不可变类型


#Python iterator
import sys
list=[1,2,3,4]
it=iter(list) # create iterator object by Python
print(next(it)) # print single element

# for item in list:
#     print(item)
'''
while True:
    try:
        print(next(it))
    except StopIteration:
        sys.exit()
'''
#define a iterator object
class MyNumber:
    def __iter__(self):
       self.a=1
       return self
    def __next__(self):
        if self.a <=20:
            x=self.a
            self.a +=1
            return x
        else:
            raise StopIteration

myclass=MyNumber()
myiter= iter(myclass)

for i in myiter:
    print(i)

# create generator(在 Python 中，使用了 yield 的函数被称为生成器（generator）。)
# 跟普通函数不同的是，生成器是一个返回迭代器的函数，只能用于迭代操作，更简单点理解生成器就是一个迭代器。
# 在调用生成器运行的过程中，每次遇到 yield 时函数会暂停并保存当前所有的运行信息，返回 yield 的值, 并在下一次执行 next() 方法时从当前位置继续运行。

# 调用一个生成器函数，返回的是一个迭代器对象。
import sys
def fibonacci(n):
    a,b,counter=0,1,0
    while True:
        if(counter>n):
            return
        yield a
        a,b=b,a+b
        counter +=1

f=fibonacci(10)

while True:
    try:
        print(next(f),end=" ")
    except StopIteration:
        sys.exit()