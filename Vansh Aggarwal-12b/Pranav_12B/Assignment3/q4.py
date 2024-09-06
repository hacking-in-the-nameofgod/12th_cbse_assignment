"""PRANAV PRADEEP
ASSIGNMENT 3: Q 2: 4/6/24"""
import csv
import os

def create_file():
    f = open("Travel.csv", "a", newline = "")
    f.close()


def store():
    f = open("Travel.csv", "a", newline = "")
    l = []
    l.append(input("Place_name"))
    l.append(input("Country"))
    l.append(int(input("TravelCost")))
    l.append(input("MiscCost"))

    fout = csv.writer(f)
    fout.writerow(l)
    f.close()
    print ("Data stored")

def display():
    f = open("Travel.csv", "r")
    fin = csv.reader(f)
    print(f'{"Place_Name":20}{"Country":20}{"TravelCost":20}{"MiscCost":20}{"Sum ":20}')
    for i in fin:
        print (f'{i[0]:20}{i[1]:20}{i[2]:20}{i[3]:20}{int(i[2])+int(i[3])}')

def delete():
    n = input("Enter place to be deleted ")
    f = open("Travel.csv", "r")
    f1 = open("temp.csv", "w", newline = "")
    fin = csv.reader(f)
    fout = csv.writer(f1)
    for i in fin:
        if i[0] != n:
            fout.writerow(i)
    f.close()
    f1.close()

    os.remove("Travel.csv")
    os.rename("temp.csv", "Travel.csv")

create_file()
while True:
    a = input('''
1) Add more rows
2) Display all the records
3) Delete a particular record
4) Break
''')
    
    a = input("enter what you want to do ")
    if a == "1":
        store()
    if a == "2":
        display()
    if a == "3":
        delete()
    if a == "4":
        break


        
