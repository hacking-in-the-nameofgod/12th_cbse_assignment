"""nIGGA WASSUP" DFGH TROEKNLJND"""
import pickle
def create_file():
    f = open("movie.dat", "ab")
    f.close()

def store_data():
    f = open("movie.dat", "ab")
    l = []
    l.append(input("enter movie name "))
    l.append(input("enter language "))
    l.append(int((input("enter movie rating "))))
    pickle.dump(l,f)
    f.close()

def read_data():
    f = open("movie.dat", "rb")
    try:
        while True:
            data = pickle.load(f)
            print(data)

    except EOFError:
        print("file read")
        f.close()

def search():
    f = open("movie.dat", "rb")
    max = 0
    a = ''
    while True:
        try:
            data = pickle.load(f)
            if data[2] > max:
                max = data[2]
                a = data[0] 
        except EOFError:
            break
    print ("the highest rated movie is ", a, " with a rating ", max)

create_file()
while True:
    a = input("enter what you want to do ")
    if a == "a":
        store_data()
    if a == "b":
        read_data()
    if a == "c":
        search()
    if a == "d":
        break




  
