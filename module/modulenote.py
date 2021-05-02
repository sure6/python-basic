# in python,  package(one folder or subpackage) --> module(one filename.py as one module)--> class(general only one), varibles, methods
# in python, programmer can initiate module authority control. use __all__ =[put str type of all name that other module enable to access ]
""" 
    package and namespace: in python, programmer build a package and build a __init__.py file in the package. 
    after importing the package, the code in __init__ .py will run automatically. Alse, when variable and methods have same name, 
    programmer can use different namespace to mark same variblename or methodname.if both are same, the later will cover the former
    under some general situation, programmer can use __init__.py to add default import other module,which can avoid to repeat importing
"""
# path search:later learn  

""" 
avoid to loop importing, for instance: module1 import module2, module2 import module3, module3 import module1
"""

"""
in python, there are some module from  thirdparty. when we want to know what the thirdparty modules are in local computer, we can use instruction
(pip list) in cmd wndow OS or (use help('modules')  to see all module in IDLE) . if want to install/uninstall, use instruction (pip install/uninstall (the thirdparty modules name))
"""

""" 
if __name__ == "__main__": # 每个模块都有一个__name__属性，当其值是'__main__'时，表明该模块自身在运行，否则是被引入。这样可以以主程序进行调试
    print("a")
else:
    print("b")

"""