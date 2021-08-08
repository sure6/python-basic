import pickle
import json


class Student:
    def __init__(self, name, age, score):
        self.name = name
        self.age = age
        self.score = score


s = Student("leesure", 25, 99)
with open("lx1.txt", "w") as f:
    json.dump(s,f,default=lambda s:s.__dict__)
    # print(pickle.load(f).name)
