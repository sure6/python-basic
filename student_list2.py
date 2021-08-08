"""
date: 2021/4/26 23:47
author: lee sure
"""
# Enter student file name: student_list.txt
# Enter 1st column length: 20
# Enter 2nd column length: 21
# Enter 3rd column length: 22
import csv

student_path=input("Enter student file name: ")
first_col=input("Enter 1st column length: ")
second_col=input("Enter 2nd column length: ")
third_col=input("Enter 3rd column length: ")
output_format="{0:<"+first_col+"}{1:^"+second_col+"}{2:>"+third_col+"}"
print(output_format.format("code", "name", "cp"))
with open(student_path, "r") as f:
    reader = csv.DictReader(f)
    for row in reader:
        student_code=row.get("code")
        s_name=row.get("name")
        s_cp=row.get("cp")
        print(output_format.format(student_code, s_name,s_cp))