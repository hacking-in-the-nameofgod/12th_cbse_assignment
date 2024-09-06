"""
Assignment 2 Question 3 done by Vansh Aggarwal
Date: 5/4/24 
Time of start: 12:44
"""

#Top-Level Variable Assignment
import os

#Function Creation
def create_file():
    f = open("poem.txt", "w")
    f.close()
    print("File Created")

#check file
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


def add_content(content):
    f = open("poem.txt", "a")
    f.write(content + "\n")
    f.close()
    print ("Content has been added. ")

def display_content():
    final = []
    f = open("poem.txt", "r")
    data = f.readlines()
    f.close()
    for i in data:
        final.append(i.rstrip("\n"))
    return(final)

def count_word(word):
    data = display_content()
    temp_count = 0
    for i in data:
        if word in i:
            temp_count += i.count(word)

    return (temp_count)

def remove_line(alphabet):
    data = display_content()
    fout = open("temp.txt", "w")
    fout.close()
    fout = open("temp.txt", "a")
    for i in data:
        if i != '' and i[0][0] != alphabet:
            fout.write(i + "\n")
    fout.close()
    os.remove("poem.txt")
    os.rename("temp.txt", "poem.txt")
    print("Lines Removed")

def file_size():
    data = display_content()
    count = 0
    for i in data:
        for j in i:
            count +=1

    return (count)

def used_word():
    data = display_content()
    output = "temp word"

    for i in data:
        line = i.split()
        for j in line:
            temp = count_word(j)
            if temp > count_word(output):
                output = j

    return (output)
                

def remove_extra():
    
    fout = open("rice.txt", "w")
    fout.close()
    fout = open("rice.txt", "a")
    data = display_content()
    for i in data:
        line = i.split()
        new_line = ''
        for j in line:
            new_line = new_line + j + " "
        fout.write(new_line + "\n")
    fout.close()
    os.remove("poem.txt")
    os.rename("rice.txt", "poem.txt")


        
            
while True:
    print( """
Options:
1) Add more content to the file.  
2) Display the entire file content 
3) Count the number of times a particular word is present in the file.
4) Remove the lines which start with a particular alphabet.  
5) Display the size of the file. 
6) Display the most used word from the file.
7) Remove the extra spaces and blank lines from the file.
8) Exit
""")

    opt1 = int(input("Enter the option number: "))

    if opt1 ==1:
        append_str = input("Enter the content to be appended:  ")
        add_content(append_str)

    elif opt1==2:
        print()
        print()
        data = display_content()
        for i in data:
            print (i)
    elif opt1==3:
        wrd = input("Enter the word to be counted: ")
        word_count = count_word(wrd)
        print (word_count)
    elif opt1==4:
        al = input("Enter the alphabet: ")
        remove_line(al)
    elif opt1==5:
        cnt = file_size()
        print ("The file size is: ", cnt)
    elif opt1==6:
        most_used = used_word()
        print (most_used)
    elif opt1==7:
        remove_extra()
        print ("Extra Spaces Removed. ")

    elif opt1==8:
        print("The program will now exit.")
        break
    else:
        print("Not a valid input.")
        print("Please try again.")