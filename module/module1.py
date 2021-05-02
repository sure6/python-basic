""" import sys

print("'命令行参数如下:'")

for i in sys.argv:
    print(i)

print("\n\npython路径为: ",sys.path, "\n") """

__all__ =['a','Add', 'Caculation'] # b cannot be accessed

a=1
b=2

def Add(num1,num2):
     return num1+num2

class Caculation:
    def __init__(self, num1, num2):
        self.num1=num1
        self.num2=num2

    def Add(self):
        return self.num1+self.num2

# print(__name__)
if __name__ == "__main__":
    print("a is" +str(a))