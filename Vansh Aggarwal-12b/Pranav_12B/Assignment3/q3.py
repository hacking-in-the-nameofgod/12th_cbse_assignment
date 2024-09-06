"""PRANAV PRADEEP
ASSIGNMENT 3: Q 3: 8/6/24"""
import csv

def create_file():
    f = open("Emp.csv", "a")
    f.close()


def store():
    f = open("Emp.csv", "a", newline = "")
    l = []
    l.append(input("Ename"))
    l.append(input("Eid"))
    l.append(int(input("Esal")))
    l.append(input("Department"))
    fout = csv.writer(f)
    fout.writerow(l)
    print("Data Stored ")

def display():
    f = open("Emp.csv", "r", newline = "")
    fin = csv.reader(f)
    for i in fin:
        print ((f'{i[0]:20}{i[1]:20}{i[2]:20}{i[3]:20}'))

def search():
    f = open("Emp.csv", "r", newline = "")
    b = input("enter name")
    fin = csv.reader(f)
    for i in fin:
        if i[0] == b:
            print (i)
            break
    else:
        print("Employee not found")

def search_dep():
    f = open("Emp.csv", "r", newline = "")
    b = input("enter department name")
    while True:
        a = csv.reader(f)
        for i in a:

            if i[3] == b:
                print (i)
                break
        else:
            print ("Department not found")

def sort():
    f = open("Emp.csv", "r", newline = "")
    lo = []
    l = []
    while True:
        a = f.readline()
        if a:
            l = a.split(",")
            lo.append(l[2])
        else:
            break
    b = f.readlines()
    for i in range (len(lo)):
        for j in range ((len(lo))- i -1):
            if lo[j]>lo[j+1]:
                lo[j], lo[j+1] = lo[j+1], lo[j]
                b[j], b[j+1] = b[j+1], b[j]
    for i in b:
        print (i)

create_file()
while True:
    a = input('''
1) Add more rows
2) Display All
3) Search for a particular employee
4) Display all the employees in a particular department
5) Sort the employee as per their salary and display.
''')
    
    a = input("enter what you want to do ")
    if a == "1":
        store()
    if a == "2":
        display()
    if a == "3":
        search()
    if a == "4":
        search_dep()
    if a == "5":
        sort()
    if a == "6":
        break


        






