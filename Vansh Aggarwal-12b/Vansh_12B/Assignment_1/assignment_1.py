"""
Assignment 1 Question 1 done by Vansh Aggarwal
Date: 6/3/24 
Time of start: 13:22

"""

#import 

import random


# take inputs

temp = "ABCFGHLJPT"
i=1
name = input("Enter name: ")

print ('''
o A Stands for Association of Persons (AOP) 
o B Stands for Body of Individuals (BOI) 
o C Stands for Company 
o F Stands for Firm 
o G Stands for Government 
o H Stands for HUF (Hindu Undivided Family) 
o L Stands for Local Authority 
o J Stands for Artificial Judicial Person 
o P Stands for Individual 
o T Stands for AOP (Trust)
    ''')
opt1 = input("Enter Letter of category: ")

# define all the functions


def check_3letters():
    x1 = random.randint(65,90)
    x2 = random.randint(65,90)
    x3 = random.randint(65,90)

    l3 = chr(x1) + chr(x2) + chr(x3)

    return(l3)


def check_4letter(o1):
    global opt1

    while True:
        if opt1 in temp:
            return(opt1)
        else:
            opt1 = str(input("Enter Letter of category: "))


def check_letter5(name):
    l = name.split()
    return(l[len(l)-1][0])


def seq_num():
    n1= str(random.randint (0,9))
    n2= str(random.randint (0,9))
    n3= str(random.randint (0,9))
    n4= str(random.randint (0,9))

    seq = n1+n2+n3+n4
    return (seq)

def check_digit (PAN):
    sum = 0
    for i in PAN:
        if ord(i)>= 65 and ord(i) <= 90:
            sum += ord(i)-65
        
        else:
            sum += int(i)
    rem = (sum%26) +64
    let = chr(rem)
    return (let)


# Main Loop for all functions

for i in range (5):
    PAN = str(check_3letters()) + str(check_4letter(opt1)) + str(check_letter5(name)) + str(seq_num())
    check = check_digit (PAN)

    print ("Possible PAN number" , i+1, PAN + check)


    