"""PRANAV PRADEEP
ASSIGNMENT 3: Q 2: 4/6/24"""
import pickle
import os

def create_file():
    f = open("product.dat", "ab")
    f.close()

def store_data():
    f = open("product.dat", "ab")
    d = {}
    d["Pid"] = (input("enter product id "))
    d["Pname"] = (input("enter product name "))
    d["Qty"] = (int((input("enter quantity "))))
    d["Price"] = (int((input("enter price "))))
    pickle.dump(d,f)
    f.close()
    print("product stored")

def read_data():
    f = open("product.dat", "rb")
    print()
    print (f'{"Product Id":20}{"Product name":20}{"Quantity":20}{"Price":20}')
    try:
        while True:
            data = pickle.load(f)
            
            print(f'{data["Pid"]:20}{data["Pname"]:20}{data["Qty"]:8}{data["Price"]:17}')


    except EOFError:
        print()
        print("file read")
        f.close()

def search_data():
    f = open("product.dat", "rb")
    n = input("enter product name ")
    
    while True:
        try:
            data = pickle.load(f)
            if data["Pname"] == n:
                print (f'{"Product Id":20}{"Product name":20}{"Quantity":20}{"Price":20}')
                print(f'{data["Pid"]:20}{data["Pname"]:20}{data["Qty"]:8}{data["Price"]:17}')

                break
        except EOFError:
            print ("file not found")
            break

def update_data():
    f = open("product.dat", "rb")
    n = input("Enter name to update: ")
    fout = open("Temp0.dat", "wb")
    try:
        while True:
            data = pickle.load(f)
            if data["Pname"] == n:
                print (data)
                data["Price"] = float(input("Enter new price: "))
                pickle.dump(data, fout)
                break
        while True:
            data = pickle.load(f)
            if data["Pname"] != n:
                pickle.dump(data, fout)

    except EOFError:
        print()
    finally:
        print("updated")
        f.close()
        fout.close()
        os.remove("product.dat")
        os.rename("temp0.dat", "product.dat")


def delete():
    n = input("Enter Pid to be deleted: ")
    f = open("product.dat", "rb")
    fout = open("temp.dat", "wb")
    try:
        while True:
            data = pickle.load(f)
            if data["Pid"] != n:
                pickle.dump(data, fout)
    except:
        f.close()
        fout.close()
        print ("item deleted ")
    finally:
        os.remove("product.dat")
        os.rename("temp.dat", "product.dat")

def move():
    n = input("Enter Pid to be moved: ")
    f = open("product.dat", "rb")
    fout = open("temp.dat", "wb")
    fout2 = open("temp2.dat", "wb")
    try:
        while True:
            data = pickle.load(f)
            if data["Pid"] == n:
                pickle.dump(data, fout)
            else:
                pickle.dump(data, fout2)
    except:
        print("item moved")
        f.close()
        fout.close()
        fout2.close()
        os.remove("product.dat")
        os.rename("temp2.dat", "product.dat")

create_file()
while True:
    a = input("""

The menu options are:-
1) Add more data
2) Display All
3) Search for a product by name
4) Update the product price
5) Delete the product
6) Move certain products (by name) to a separate file: 
7) Break
""")
    if a == "1":
        store_data()
    if a == "2":
        read_data()
    if a == "3":
        search_data()
    if a == "4":
        update_data()
    if a == "5":
        delete()
    if a == "6":
        move()
    if a == "7":
        break

