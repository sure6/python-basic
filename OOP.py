# 3 characteristics for class: inheritance, encapsulation, polymorphisms
# 3 characteristics for object: value id type - corresponded to 3 compare methods-> == is isintance
# access authority: attrName or methodName->public, _attrName or _methodName->protect, __attrName or __methodName->private. Also, classname can add _ or __

# instance attr and class attr
'''
class Student:
    age = 66
    def __init__(self, name):
        self.name=name

s = Student("Bob")
s.score=60
print(s.score)
print(s.age)
m = Student("mary")
m.age=10 # don't suggest to add same instance attr and class  attr name  
print(m.age)
print(Student.age)
'''

# py is a dynamic language(enable to add new attributes and methods when programming run)
# this is different with C/C++ and JAVA (static language: must distribute the size of memory before running)

# under normal circumstance,  we can add attrs in a instance
# we can also add a methods to bond with the instance, but only usable in the instance, it is not usable to change another instance
# Also, we can add a methods in a class, which can make every instance use the methods
'''
class Student(object):
    __slots__=("name","age")
    pass
'''

'''
def set_age(self, age):
    self.age=age

from types import MethodType 
s=Student()
s.set_age = MethodType(set_age, s)
print(s.set_age)
s.set_age(20)
print(s.age)
'''
# in order to constrain attr added in a instance ,we can add __slots__ in class
# 使用__slots__要注意，__slots__定义的属性仅对当前类实例起作用，对继承的子类是不起作用的：
'''
s= Student()
s.name="lesure"
s.age=90
s.scrore=89 # error
'''
# @property usage
'''
class Student(object):
    @property # convert a getter() to an attr
    def grade(self):
        return self._grade
    
    @grade.setter # convert a setter() to an attr
    def grade(self,value):
        if not isinstance(value, int):
            raise ValueError("grade must be integer!")
        if value <0 or value >100:
            raise ValueError("grade must be between 0~100")
        self._grade = value

s = Student()
s.grade=60
print(s.grade)
'''
# exercise
# 请利用@property给一个Screen对象加上width和height属性，以及一个只读属性resolution：
'''
class Screen(object):
    pass
    @property
    def width(self):
        return self._width
    @width.setter
    def width(self,value):
        if value <0 :
            raise ValueError("width can be negative")
        self._width=value
    @property
    def height(self):
        return self._height
    @height.setter
    def height(self,value):
        if value <0 :
            raise ValueError("width can be negative")
        self._height=value
    @property
    def resolution(self):
        return self._width *self._height

s = Screen()
s.width = 1024
s.height = 768
print('resolution =', s.resolution)
if s.resolution == 786432:
    print('测试通过!')
else:
    print('测试失败!')
'''

# python support multi-inheritance
# 在设计类的继承关系时，通常，主线都是单一继承下来的，例如，Ostrich继承自Bird。但是，如果需要“混入”额外的功能，通过多重继承就可以实现，
# 比如，让Ostrich除了继承自Bird外，再同时继承Runnable。这种设计通常称之为MixIn。
# 单一继承语言不支持MixIn(如java)

# customize class
'''
class Student:
    def __init__(self,name):
        self._name=name
    def __str__(self):
        return "Student object (name:{})".format(self._name)
    def __repr__(self):
        return "Student object"
    # def __getattribute__(self, name):
    #     if name =="age":
    #         return 22
    ''''''
    一个对象实例可以有自己的属性和方法，当我们调用实例方法时，我们用instance.method()来调用。能不能直接在实例本身上调用呢？在Python中，答案是肯定的。
    任何类，只需要定义一个__call__()方法，就可以直接对实例进行调用,并且不能与__getattribute__共存
    ''''''
    def __call__(self):
        print("my name is {}".format(self._name))

s=Student("leesure") # default call __repr__. if defining a __str__ , displaying content in __str__
# print(s)
# print(s.score) # none because override original __getattribute__, cannot display error
# print(s.age)
s()
# 通过callable()函数，我们就可以判断一个对象是否是“可调用”对象。
# 那么，怎么判断一个变量是对象还是函数呢？其实，更多的时候，我们需要判断一个对象是否能被调用，能被调用的对象就是一个Callable对象，
# 比如函数和我们上面定义的带有__call__()的类实例
print(callable(s))
print(callable([1,2,3,4]))
'''



'''
class Fib:
    def __init__(self):
        self._a, self._b=0,1
    def __iter__(self): # instance is a iterable object,so return myself
        return self
    def __next__(self):
        self._a,self._b=self._b,self._a+self._b
        if self._a >1000:
            raise StopIteration()
        return self._a
    # note: this object doesn't completely see as a List, because it cannot choose certain element through index. such as Fib()[5] error 
    # but developers can use __getitem__() to achieve
    def __getitem__(self,index):
        for i in range(index):
            self._a,self._b=self._b,self._a+self._b
        return self._a


for i in Fib():
    print(i, end=", ")
print()
print(Fib()[3])
'''
'''
也没有对负数作处理，所以，要正确实现一个__getitem__()还是有很多工作要做的。

此外，如果把对象看成dict，__getitem__()的参数也可能是一个可以作key的object，例如str。

与之对应的是__setitem__()方法，把对象视作list或dict来对集合赋值。最后，还有一个__delitem__()方法，用于删除某个元素。

总之，通过上面的方法，我们自己定义的类表现得和Python自带的list、tuple、dict没什么区别，这完全归功于动态语言的“鸭子类型”，不需要强制继承某个接口。
'''

# use __getattr__() to write a RESTful API
'''
class Chain:
    def __init__(self,path=""):
        self._path=path
    def __getattr__(self,path):
        return Chain("{0}/{1}".format(self._path,path))
    def __str__(self):
        return self._path

print(Chain().leesure.css.js)
'''

# Enum class

from enum import Enum,unique
'''
Month = Enum("month",('Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec'))
for name,member in Month.__members__.items():
    print(name, '->', member, ',', member.value)

# @unique装饰器可以帮助我们检查保证没有重复值。
@unique
class Weekday(Enum):
    Sun = 0 # Sun的value被设定为0
    Mon = 1
    Tue = 2
    Wed = 3
    Thu = 4
    Fri = 5
    Sat = 6
'''
# exercise
# 把Student的gender属性改造为枚举类型，可以避免使用字符串：
'''
@unique
class Gender(Enum):
    Male = 0
    Female=1


class Student:
    def __init__(self,name, gender):
        self._name=name
        self._gender=gender
    # @property # this is a attr label, if using, access by object.attr, otherwise by object.methodName()
    def gender(self):
        return self._gender
    

s=Student("leesure", Gender.Male.value)
print(Gender.Male.value)
print(s.gende)
'''


'''
class Student:
    class SubStudent:
        def __init__(lee,name, age):
            lee._name=name
            lee._age=age
    def getSubStudent(self):
        return self.SubStudent("leesure", 16)
    def getSubStudentName(self):
        return  self.getSubStudent()._name

print(Student().getSubStudentName())
'''

# use metaclass
"""
from helllo import Hello

print(Hello().hello("leesure"))
print(type(Hello))
print(type(Hello().hello))

#type()函数既可以返回一个对象的类型，又可以创建出新的类型，比如，我们可以通过type()函数创建出Hello类，而无需通过class Hello(object)...的定义：#
Introduct=type("Introduction", (object,), dict(aa=Hello().hello))
print(Introduct().aa("asda"))
print(type(Introduct()))
"""
# metaclass is very difficult to understand. so far don't require to master

"""
supplementary
"""


class Student:
    name = "lee"
    @classmethod
    def teaching(cls):
        return "dasda"+ cls.name
    @staticmethod
    def learning():
        return "dasdalee"

def learning():
    return "addsad"

print(Student.teaching())
print(Student.learning())
print(learning())

print(Student.name)
Student.name="sure" # denote that class attributes can be modified outside class
print(Student.name)

""" class Student:
    def __init__(self,id, firstName, lastName):
        self.id=id
        self.firstName =firstName
        self.lastName =lastName

class PostStudent(Student):
    def __init__(self, id, firstName, lastName, thesis):
        super().__init__(id, lastName, firstName) # No matter what the order of arguments is, it follows the order of arguments of the parent class. 

ps=PostStudent("001", "lee", "sure", "helloworld")

print(ps.firstName)
print(ps.lastName) """


""" class Student:
    __score=10
    _hello="hello" # 能访问

    def __init__(self,name,age):
        self.__name=name
        self.__age=age

s = Student("lee",29)
print(s._Student__name)# 外部访问内部私有变量
print(Student._hello)
print(s.__age)
 """
