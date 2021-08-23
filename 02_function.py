def add_name():
    first_name="Xuan"
    last_name="Li"
    return first_name, last_name

full_name = add_name()

print(full_name)

def expand(word, multiplicity):
    list1 = [x*multiplicity for x in word]
    str1=""
    it= iter(list1)
    for i in it:
        str1 +=i
    return str1

# print(expand("word",2))

def transform_character(letter):
    if letter == "i" or letter == "I":
        return 1
    elif letter == "r" or letter == "R":
        return 7
    elif letter == "s" or letter == "S":
        return 5
    elif letter == "z" or letter == "Z":
        return 2
    else:
        return letter

print(type(transform_character("w")))

def factorial(n):
    if n==1:
        return 1
    else:
        return n*factorial(n-1)

print(factorial(6))

def next_number(number):
    if number%2==0:
        return 3*number +1
    else:
        return 2* number +2

print(next_number("6"))