# no return => return None
# don't define func name same with internal function name
# in python, function can return multiply values ,but greater than 2 values, return a tuple type
# define parameters requirement: first essential para, then keywords para

# Sequence unpacking
""" a, b, c = 1, 2, 3
print(a, b, c)

d = 1, 2, 3
print(d)# tuple

a, b, c = d


a, b = d  # error """
""" 
def add(a,b=2): # default parameter
    print("a=",a)
    print("b=",b)
    return a+b

# print(add(b=1,a=2))
print(add(a=2)) """

""" def print_menu(waiter, place_no,*value): # python3.8.8 will not allow variable para put in first place if parameters have essential paras. previous vesion can put randomly
    print("this is no."+place_no)
    for i in value:
        print(i)
    print("waiter is "+waiter)

print_menu("beef","mutton","deck",waiter="lee",place_no="012") #previous vesion need to use keyword-only para to call, but python3.8.8 does not. it need to first put essential paras then put varible paras """

# function varible range
a="cba" # global varible

def test():
    global a # if want to become global varible, we can use keywords global
    a="abc" # partial varible
    print("after  function be called: "+a)

print("before call:"+a)
test()
print("finished calling: " +a)