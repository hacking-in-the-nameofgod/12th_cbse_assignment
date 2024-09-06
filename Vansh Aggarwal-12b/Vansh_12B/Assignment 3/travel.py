"""
Assignment 3 Question 4 done by Vansh Aggarwal
Date: 31/7/24 
Time of start: 11:59

"""
import csv as c
import os

#create file

def create_file():
    f = open("Travel.csv", "w")
    f.close()
    f = open ("Travel.csv", "a")
    fout = c.writer(f)
    header = ["Country", "Place", "Travel Cost", "Misc Cost"]
    fout.writerow(header)
    base = [["Switzerland","Lake Geveva", 145000, 18000], ["America ","Los Angeles", 125000, 25000], ["Australia","Great Barrier Reef", 20000, 12000]]
    fout.writerows(base)
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
    fout = open ("Travel.csv", "a+")
    Country = input("Enter the Country: ")
    Place = input("Enter the Place: ")
    Travel_Cost = int(input("Enter the Travel Cost: "))
    Misc_Cost = int(input ("Enter the Misc Cost: "))
    temp = [Country, Place, Travel_Cost, Misc_Cost]
    finput = c.writer(fout)
    finput.writerow(temp)
    fout.close()

def return_data():
    fout = open ("Travel.csv", "r")
    csvreader = c.reader(fout)
    header = [] 
    header = next(csvreader) 
    rows = []
    for row in csvreader:
        if row != []:
            rows.append(row.append (int (row[2]+row[3])))
    fout.close()

    return (header,rows)

def delete(search_string):
    header, rows = return_data()
    f = open("Travel1.csv", "w")
    f.close()
    f = open ("Travel1.csv", "a")
    fout = c.writer(f)
    header = ["Country", "Place", "Travel Cost", "Misc Cost"]
    fout.writerow(header)
    base = [["Switzerland","Lake Geveva", "145000", "18000"], ["America ","Los Angeles", "125000", "25000"], ["Australia","Great Barrier Reef", "20000", "12000"]]
    fout.writerows(base)
    for i in rows:
        if i[0] == search_string:
            element = rows.pop(i)

    fout.writerows(rows)
    f.close()

    os.remove("Travel.csv")
    os.rename("Travel1.csv" , "Travel.csv")


# Main Loop

while True: 
    print (''' 
The menu options are:- 
1) Add more rows. 
2) Display All the records and show the total cost to visit a place. 
3) Delete a particular record 
4) Exit
''')
    opt1 = int(input("Enter the option to execute: "))

    if opt1==1:
        add_row()
    elif opt1 ==2:
        header, data = return_data()
        print (f'{header[0]:30}{header[1]:30}{header[2]:30}{header[3]:30}{"Total Cost":30}')
        for i in data:
            print(f'{i[0]:30}{i[1]:30}{i[2]:30}{i[3]:30}{i[4]:30}')
            print(i)
    elif opt1 ==3:
        search_string = input("Enter the Country to Delete: ")
        delete(search_string)

    elif opt1 == 4:
        print ("Exit")
        break

