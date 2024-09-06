"""
Assignment 2 Question 1 done by Vansh Aggarwal
Date: 21/3/24 
Time of start: 13:22

"""
#Top-Level Variable Assignment

final = []
opt1 = 0

up_vowel = "AEIOU"
down_vowel = "aeiou"

#Function Creation

def create_file():
    f = open("story.txt", "w")
    f.close
    print("File Created")

def store_data(append_string):
    f = open("story.txt", "a")
    f.write(append_string + "\n")
    f.close
    print("Text Added")

def read_data():
    final = []
    f = open("story.txt", "r")
    data = f.readlines()
    f.close
    for i in data:
        final.append(i.rstrip("\n"))
    return(final)

def count_alpha():
    n = 0 
    data = read_data()
    for i in data:
        for j in i:
            if j.isalpha():
                n+=1
    return(n)

def count_num():
    n = 0 
    data = read_data()
    for i in data:
        for j in i:
            if j.isdigit():
                n+=1
    return (n)

def count_space():
    n = 0 
    data = read_data()
    for i in data:
        for j in i:
            if j == " ":
                n+=1
    return (n)

def count_special():
    n = 0 
    data = read_data()
    for i in data:
        for j in i:
            if j != " " and not(j.isalpha()) and not(j.isdigit()) :
                n+=1
    return (n)

def count_upper_vowel():
    n = 0 
    data = read_data()
    for i in data:
        for j in i:
            if j in up_vowel :
                n+=1
    return (n)

def count_lower_vowel():
    n = 0 
    data = read_data()
    for i in data:
        for j in i:
            if j in up_vowel :
                n+=1
    return (n)

def count_consonant():
    n = 0 
    data = read_data()
    for i in data:
        for j in i:
            if j not in up_vowel and j not in down_vowel and j.isalpha():
                n+=1
    return (n)

def count_lines():
    n = len(read_data())
    return (n)

def count_words():
    n = 0 
    data = read_data()
    for i in data:
        l = i.split()
        n +=len(l)
    return(n)

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


#Main loop

while opt1 != 6:
        
    print ("""
The menu options are:-
1) Add more content to the file.
2) Display the entire file content
3) No. of different types of characters used
4) No. of uppercase, lowercase vowels and no.of consonants
5) No. of words and No. of lines
6) Exit 
""")

    opt1 = int(input("Enter the option no: "))

    if opt1 == 1:
        appendage = input ("Enter the string to be added: ")
        store_data(appendage)
    
    elif opt1 == 2:
        for i in read_data():
            print (i)

    elif opt1 == 3:
        print ("The number of Alphabets used in the given file is: ", count_alpha())
        print ("The number of Numbers used in the given file is: ", count_num())
        print ("The number of Spaces used in the given file is : ", count_space())
        print ("The number of Special Characters used in the given file is: ", count_special())

    elif opt1 == 4:
        print("The number of Uppercase Vowels are: ", count_upper_vowel())
        print ("The number of Lowercase Vowels are: ", count_lower_vowel())
        print ("The number of consonants are: ", count_consonant())

    elif opt1 == 5:
        print ("The number of words are: ", count_words())
        print ("The number of lines are:", count_lines())
    elif opt1 == 6:
        print ("The program will Exit now.")
        break
    else:
        print("Invalid Input. Try again")
