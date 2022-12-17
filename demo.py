# The 1st column must use right alignment.
# The 2nd column must use center alignment.
# The 3rd column must use left alignment.
# The 4th column must use right alignment.

# file name: book.csv
# Enter 1st column length: 15
# Enter 2nd column length: 25
# Enter 3rd column length: 20
# Enter 4th column length: 10


import csv

f_name=input("Enter file name: ")
f_col=input("Enter 1st column length: ")
s_col=input("Enter 2nd column length: ")
t_col=input("Enter 3rd column length: ")
four_col=input("Enter 4th column length: ")

print(("{0:>"+f_col+"}{1:^"+s_col+"}{2:<"+t_col+"}{3:>"+four_col+"}").format("Location","Book title","Publication Date", "Available"))

with open(f_name,'r') as f:
    reader = csv.DictReader(f)

    for row in reader:
        shelf= row.get('SHELF')
        title= row.get('TITLE')
        date= row.get('DATE')
        avail= row.get('AVAILABLE')
        print(("{0:>"+f_col+"}{1:^"+s_col+"}{2:<"+t_col+"}{3:>"+four_col+"}").format(shelf,title,date,avail))