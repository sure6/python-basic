import module1

a = module1.fib(100) # why? when using print function, the return can appear None on next line?
a
print(module1.fib2(100))


if __name__ == "__main__": # 每个模块都有一个__name__属性，当其值是'__main__'时，表明该模块自身在运行，否则是被引入。
    print("a")
else:
    print("b")