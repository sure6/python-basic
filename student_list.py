"""
date: 2021/4/26 23:47
author: lee sure
"""
# Enter student file name: student_list.txt
# Enter 1st column length: 20
# Enter 2nd column length: 21
# Enter 3rd column length: 22

student_path=input("Enter student file name: ")
first_col=input("Enter 1st column length: ")
second_col=input("Enter 2nd column length: ")
third_col=input("Enter 3rd column length: ")
output_format="{0:>"+first_col+"}{1:>"+second_col+"}{2:>"+third_col+"}"
print(output_format.format("Student Number", "First Name", "Last Name"))
with open(student_path, "r") as f:
    while True:
        student_no = f.readline().strip("\n")
        if not student_no:
            break
        f_name=f.readline().strip("\n")
        l_name=f.readline().strip("\n")
        print(output_format.format(student_no, f_name,l_name))