"""
Assignment 3 Question 2 done by Vansh Aggarwal
Date: 21/6/24 
Time of start: 11:29

"""
import pickle as p
import os

#create file

def create_file():
    f = open("product.dat", "wb")
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

def addproduct():
    fout = open("product.dat", "ab")
    pid = int(input("Enter product ID:"))
    pname = input("Enter Product Name: ")
    qty = int(input("Enter Quantity of the product: "))
    price = float(input("Enter Price of product: "))
    product = {"pid":pid,"pname":pname, "qty":qty, "price":price}
    p.dump(product, fout)
    fout.close()

def readproduct():
  data = []
  try:
    with open("product.dat", "rb") as fout: 
      while True:
        data_1 = p.load(fout)
        data.append(data_1)
  except EOFError:
    print()
  finally:
    fout.close() 
    return(data)

def searchproduct(search_string):
    data = readproduct()
    for i in data:
        if i["pname"] == search_string:
            return(i)
    else:
        return("No such product found. ")

def update_price(search_string):
    fout = open("product1.dat", "wb")
    fout.close()
    ################################
    fout = open("product1.dat", "ab")
    data = readproduct()
    for i in data:
        if i['pname'] != search_string:
            p.dump(i,fout)
        elif i['pname'] == search_string:
            new_price = float(input("Enter the new price: "))
            i["price"] = new_price
            p.dump(i,fout)
    
    fout.close()
        
    os.remove("product.dat")
    os.rename("product1.dat", "product.dat")
    print ("changes made")

def del_product(search_string):
    fout = open("product1.dat", "wb")
    fout.close()
    ################################
    fout = open("product1.dat", "ab")
    product = searchproduct(search_string)
    data = readproduct()
    for i in data:
        if i != product:
            p.dump(i,fout)
    
    fout.close()
    
    os.remove("product.dat")
    os.rename("product1.dat", "product.dat")
    
    print ("Lines deleted")

def move_product(search_string):
    fout = open("product2.dat", "wb")
    fout.close()
    ################################
    fout = open("product2.dat", "ab")
    #################################
    fin = open("product1.dat", "wb")
    fin.close()
    ################################
    fin = open("product1.dat", "ab")
    product = searchproduct(search_string)
    data = readproduct()
    for i in data:
        if i == product:
            p.dump(i,fout)
        
        if i != product:
            p.dump(i, fin)
        
    fin.close()
    fout.close()
    os.remove("product.dat")
    os.rename("product1.dat", "product.dat")

    print ("Lines moved. ")

#Main Loop: 

while True: 
    print (''' 
Options: 
1) Add more data 
2) Display All
3) Search for a product by name 
4) Update the product price
5) Delete the product
6) Move certain products (by name) to a separate file.''' )

    opt1 = int(input("Enter the option to execute: "))

    if opt1==1:
        addproduct()
    
    elif opt1 ==2:
        data = readproduct()
        for i in data:
            print (i)

    elif opt1 ==3:
        search_string= input("Enter the product to search: ")
        required_p = searchproduct(search_string)
        print (required_p)
    
    elif opt1 == 4:
        search_string= input("Enter the product: ")
        update_price(search_string)
    
    elif opt1 == 5: 
        search_string= input("Enter the product: ")
        del_product(search_string)

    elif opt1 == 6:
        n = int(input("Enter the number of items to move: "))
        for i in range (n):
            search_string= input("Enter the product: ")
            move_product(search_string)
    
    elif opt1 ==7:
        break