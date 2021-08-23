# week1

# enter1=input("Enter number of cows to purchase: ")
# cows_val= int(enter1)*30
# enter2=input("Enter number of ducks to purchase: ")
# ducks_val=int(enter2)*5
# enter3=input("Enter number of chicken to purchase: ")
# chicken_val=int(enter3)*3

# print("Cost:")
# print(enter1+" cow = "+str(cows_val)+" grassies")
# print(enter2+" duck = "+str(ducks_val)+" grassies")
# print(enter3+" chick = "+str(chicken_val)+" grassies")
# print("Total = "+ str(cows_val+ducks_val+chicken_val)+" grassies")


# week2
# product_code = "377B"
# product_name = "Beef Liquid Stock"
# product_size = "250mL"
# product_price = 2.15

# print(product_code+": "+product_name+", "+product_size)
# print(product_name+", "+product_size+", "+"$"+str(product_price))

# print("{0}: {1}, {2}".format(product_code,product_name,product_size))
# print("{0}, {1}, ${2}".format(product_name,product_size,product_price))

# print("{0:>10}{1:^30}{2:<10}".format("Faces","Name","Vertices"))
# print("{0:>10}{1:^30}{2:<10}".format(4,"Tetrahedron",4))
# print("{0:>10}{1:^30}{2:<10}".format(6,"Cube",8))
# print("{0:>10}{1:^30}{2:<10}".format(8,"Octahedron",6))
# print("{0:>10}{1:^30}{2:<10}".format(12,"Dodecahedron",20))
# print("{0:>10}{1:^30}{2:<10}".format(20,"Icosahedron",12))

# stage 2
# order = ["a","b", 1, 1.2,"bb","cc"]

# print(order[0:4:2])
# print(order[::])


# set1={"google",1,"adasad",1.1,"aad","adasad"}
# print(set1)

# a=[1,2,3]
# b=a[:]
# print(id(a))
# print(id(b))
# print(a is b)
# print(a == b)

# dict = {'Name': 'Runoob', 'Age': 7, 'Class': 'First'}

# del dict['Name']
# print(dict)

# dict = {('Name','alias'): 'Runoob', 'Age': 7, 'Class': 'First'}

# print(dict)
# print(dict[('Name','alias')])
# print(dict['Name','alias'])

# while(True):
#     print("welcome to come on my world! ")

'''
num1_str = input("Enter the first integer: ")
num1 = int(num1_str)
num2_str = input("Enter the second integer: ")
num2 = int(num2_str)
num3_str = input("Enter the third integer: ")
num3 = int(num3_str)
num4_str = input("Enter the fourth integer: ")
num4 = int(num4_str)

num_max = num1
if num_max < num2:
    num_max = num2

if num_max < num3:
    num_max = num3

if num_max < num4:
    num_max = num4

num_min = num1
if num_min > num2:
    num_min = num2

if num_min > num3:
    num_min = num

if num_min > num4:
    num_min = num4

print("The minimum number is {0} and the maximum number is {1}.".format(
    num_min, num_max))
'''
'''
li=[]
num1_str = input("Enter the first integer: ")
num1 = int(num1_str)
li.append(num1)
num2_str = input("Enter the second integer: ")
num2 = int(num2_str)
li.append(num2)
num3_str = input("Enter the third integer: ")
num3 = int(num3_str)
li.append(num3)
num4_str = input("Enter the fourth integer: ")
num4 = int(num4_str)
li.append(num4)

print("The minimum number is {0} and the maximum number is {1}.".format(
    min(li), max(li)))
'''
'''
# 10 2 15 15
li=[]
num1_str = input("Enter the first integer: ")
num1 = int(num1_str)
li.append(num1)
num2_str = input("Enter the second integer: ")
num2 = int(num2_str)
li.append(num2)
num3_str = input("Enter the third integer: ")
num3 = int(num3_str)
li.append(num3)
num4_str = input("Enter the fourth integer: ")
num4 = int(num4_str)
li.append(num4)


max_num = li[0] # 10 10 15 15
min_num = li[0] # 10 2 2 2
for item in li: # 10 2 15 15
    if item == max_num or item == min_num:
        continue
    if max_num < item:
        max_num = item
    if min_num > item:
        min_num =item
print("The minimum number is {0} and the maximum number is {1}.".format(
   min_num, max_num))
'''
