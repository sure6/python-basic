
def update_list_value(number_list):
#{
    # write your code here to increase
    # each number in the number_list by 100
    j=0
    for i in number_list:
       number_list[j]=i+100
       j+=1

#}
number_list=[1,2,3,4]
number_list1=[2,12,53,47]
update_list_value(number_list)
print(number_list)

n=int(input("How many even number?"))
li=[]
j=0
for i in range(0,n):
    li.append(j)
    j+=2
print("asdad: ",li)


fruit_list = ["Tomatoe", "Banana", "Watermelon"]

fruit_list.insert(2, "Apple")
fruit_list.insert(1, "Mango")

print(fruit_list)


def update_list_value(number_list):
#{
    # write your code here to increase
    # each number in the number_list by 100
    for i in range(0,len(number_list)):
        number_list[i]+=100

#}
list1 = [3, 8, 7]
update_list_value(list1)
print(list1)

a=[x*x for x in range(0,10)]
print(a)

def hello(x,y):
    t=0
    if x>y:
        t=x
    else:
        t=y
    if t<x:
        print("hello,world")

print(hello(1, -1))

def foo(i):
    j=i*2
    i=i+1
    i=i*j
    if(i<1):
        i=-i
    i=j/i
    return i
print(foo(-3))