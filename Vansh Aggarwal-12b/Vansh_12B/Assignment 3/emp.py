"""
Assignment 3 Question 3 done by Vansh Aggarwal
Date: 3/7/24 
Time of start: 12:11

"""
import csv as c
import os

#create file

def create_file():
    f = open("EMP.csv", "w")
    f.close()
    f = open ("EMP.csv", "a")
    fout = c.writer(f)
    header = ["EName", "EmpID", "Salary", "Department"]
    fout.writerow(header)
    f.close()
    print("File Created")

while True:
    print ("Do you want to erase the file or continue with the previous file: ")
    opt2 = int(input ("Enter 1 for yes and 2 for no: "))
    if opt2 == 1:
        create_file()
        break
    elif opt2 == 2: 
        print ("File Retained.")
        break
    else: 
        print ("Try again.")


# Main Code: 
 
def add_row():
    fout = open ("EMP.csv", "a+")
    EName = input("Enter the employee name: ")
    EmpID = int(input("Enter the employee id: "))
    Salary = float(input("Enter the salary: "))
    Department = input ("Enter the department: ")
    temp = [EName, EmpID, Salary, Department]
    finput = c.writer(fout)
    finput.writerow(temp)
    fout.close()

def return_data():
    fout = open ("EMP.csv", "r")
    csvreader = c.reader(fout)
    header = [] 
    header = next(csvreader) 
    rows = []
    for row in csvreader:
        if row != []:
            rows.append(row)
    fout.close()

    return (header,rows)

    

def Search(string):
    header,rows= return_data()
    for i in rows:
        if i [0]==string:
            return(i)
    
    else:
        return("No Record Found.")

def dept(string):
    header,rows = return_data()
    dept = []
    for i in rows:
        if i[3] == string:
            dept.append(i)
    return(dept)

def sort_():
    header,rows = return_data()
    for i in range (len(rows)):
        for j in range (len(rows)):
            if rows[i][2]<= rows[j][2]:
                rows[i], rows[j] = rows[j], rows[i]
    return (rows)


# Main Loop

while True: 
    print (''' 
Options: 
1) Add more rows 
2) Display All 
3) Search for a particular employee 
4) Display the list of all employees working in a particular department given by user. 
5) Sort the employee as per their salary and display.''' )

    opt1 = int(input("Enter the option to execute: "))

    if opt1==1:
        add_row()

    elif opt1 ==2:
        header, data = return_data()
        print (f'{header[0]:30}{header[1]:30}{header[2]:30}{header[3]:30}')
        for i in data:
            print(f'{i[0]:30}{i[1]:30}{i[2]:30}{i[3]:30}')
    
    elif opt1 ==3:
        temp_search = input ("Enter the employee name")
        employee_found = Search(temp_search)
        if employee_found != "No Record Found.":
            print(f'{employee_found[0]:30}{employee_found[1]:30}{employee_found[2]:30}{employee_found[3]:30}')
        
        else: 
            print (employee_found)
    
    elif opt1 ==4:
        temp_search = input ("Enter the department: ")
        data = dept(temp_search)
        if len(data)>1:
            for i in data:
                print (f'{i[0]:30}{i[1]:30}{i[2]:30}{i[3]:30}')
        else:
            print("Data not found. ")

    elif opt1 ==5:
        dat = sort_()
        for i in dat:
            print (f'{i[0]:30} {i[2]:30}')