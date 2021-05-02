# print(10/0)
# a=b+3

""" class TranError(Exception):
    def __init__(self, errorCode=100000, errorName="tranError"):
        self.errorCode=errorCode
        self.errorName=errorName
    def __str__(self):
        return "[%d] %s" % (self.errorCode, self.errorName)
"""
# all exception is class and inherit Exception
# after exception is triggered, the statement will finish automatically
# catch expetion
'''
try:
    # statement block
    # print("a"+2)
    raise TranError(50000,"SBError")
except (NameError, ZeroDivisionError) as e: # except + exception class as + alias
    # print(e)
    """ raise # when doesn't write Expection, is same as throwing current Exception, 并且还是要先执行完finall语句再抛出 """
except Exception  as ne: # can have some exception statement block.并且异常部分从上到下异常范围将是越来越大
    print(ne)
    print(type(ne))
else:# when no expection produce, programme can run the part
    print("expection doesn't produce")
finally: #  This statement is executed regardless of whether there is an exception
    print("resource has closed ")

print("end")
'''

""" try:
    str1=input("Enter the 1st integer: ")
    num1=int(str1)
    str2=input("Enter the 2nd integer: ")
    num2=int(str2)
    num3 = num1/num2
    print("{0} / {1} = {2}".format(num1,num2,num3))
except ValueError as ve:
    print(ve)
except ZeroDivisionError as zde:
    print("The second number must be non-zero") """

""" try:
    str1 = input("Enter a positive integer: ")
    num = int(str1)
    if(num<0):
        raise ValueError 
    print("You have entered",num)
except ValueError as e:
    print(e)
except:
    print("You have entered an invalid input") """

# i=0
# j=0
# z=0
while True:
    ua=input("Enter 1st positive number: ")
    try:
        a=int(ua)
    except:
        continue

    if(a<=0):
        continue
    else:
        # i=a
        break

while True:
    ub=input("Enter 2nd positive number: ")
    try:
        b=int(ub)
    except:
        continue

    if(b<=0):
        continue
    else:
        # j=b
        break

while True:
    uc=input("Enter 3rd positive number: ")
    try:
        c=int(uc)
    except:
        continue

    if(c<=0):
        continue
    else:
        # z=c
        break 

print("You have entered {0}, {1}, {2}".format(a,b,c))

