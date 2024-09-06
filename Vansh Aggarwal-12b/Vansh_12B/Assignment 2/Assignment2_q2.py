"""
Assignment 2 Question 2 done by Vansh Aggarwal
Date: 22/3/24 
Time of start: 12:32

"""


#Function Creation

def create_file():
    f = open("performance.txt", "w")
    f.close()
    print("File Created")

#check file presence

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

#Main Function Creation

def performance_percent(m1,m2,m3):
    percent = round(((int(m1)+int(m2)+int(m3))/3))
    return (percent)

def add_info():
    name = input("Name of Student: ")
    rollno = input ("Enter Roll No: ")
    m1 = int(input("Marks in Subject 1: "))
    m2 = int(input("Marks in Subject 2: "))
    m3 = int(input("Marks in Subject 3: "))

    percentage = performance_percent(m1, m2, m3)
    
    f = open("performance.txt", "a")
    f.write (name +" "+ rollno +" "+ str(m1) +" "+ str(m2)  +" "+ str(m3) +" "+ str(percentage) + "\n")

    f.close()
    print("Student Data Added. ")

def read_data():
    final = []
    f = open("performance.txt", "r")
    data = f.readlines()
    f.close()
    for i in data:
        j = i.split()
        final.append(j)

    return(final)

def name_percent():
    raw = read_data()
    for i in raw:
        print (f'{i[0]:<10}', ":  ", f'{i[5]:<10}')

def top3():
    raw = read_data()
    for i in range (len(raw)):
        for j in range (i):
            if raw[i][5] > raw[j][5]:
                raw [i] , raw [j]  =  raw[j], raw[i]
    
    print (raw[0][0], raw [1][0], raw[2][0], sep = "\n")

def name_search(search_str):
    raw = read_data()
    for i in raw:
        if i [0] == search_str:
            return (i)
            break
    else:
        return(None)




while True: 
    print (''' 
Options: 
1) Add Student Info 
2) Display in tabular way all students information. 
3) Display all the student name and their percentage.
4) Display the top three students as per the percentage. 
5) Search for a particular student( by name) 
6) Exit. ''' )

    opt1 = int(input("Enter the option selected: "))

    if opt1 == 1:
        add_info()

    elif opt1 ==2:
        raw = read_data()
        for i in raw:
            for j in i: 
                print (f'{j:<20}', end = " ")
            
            print ()

    elif opt1==3:
        name_percent()

    elif opt1==4:
        print ("The Top 3 Students by percentage are: ")
        top3()

    elif opt1 ==5:
        s_search = input("Enter the name: ")
        val = name_search(s_search)

        if val == None:
            print ("Name not found. ")
        else: 
            for i in val:
                print (f'{i:<9}' , end = " ")

    elif opt1 ==6:
        print("The Program will quit now.")
        break
    else:
        print ("Invalid Option. ")
        print ("Please Check Again. ")
