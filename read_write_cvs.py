"""
date: 2021/4/26 22:15
author: lee sure
"""
import csv

student_path="C:\\python-workspace\\pyFileIO\\student.cvs"

with open(student_path, 'w') as f:
    field_name_list=["stn", "first_name", "last_name"]

    writer = csv.DictWriter(f, fieldnames = field_name_list)

    writer.writeheader()
    writer.writerow({"stn":"1111", "first_name": "John", "last_name": "Smith"})
    writer.writerow({"stn":"2222", "first_name": "Lee", "last_name": "May"})
    writer.writerow({"stn":"3333", "first_name": "Ye", "last_name": "Zhang"})