import mysql.connector as mc

def createdb():
    con = mc.connect(host = "localhost", user = "root", password = "sql123")
    if con.is_connected():
        cur = con.cursor()
        cur.execute('create database institution;')
        cur.close()
        con.close()

def createtable():
    con = mc.connect(host = "localhost", user = "root", password = "sql123", database = 'institution')
    if con.is_connected():
        cur = con.cursor()
        cur.execute('use institution;')
        cur.execute('create table Faculty (TID int not NULL Primary key, FNAME varchar(30), AGE int, SUBJECT varchar(20), SALARY int, DESIGNATION varchar(20));')
        cur.close()
        con.close()

    
def store():
    con = mc.connect(host = "localhost", user = "root", password = "sql123", database = "institution")
    if con.is_connected():
        cur = con.cursor()
        while True:
            i = input("add more entry (y)/(n)")
            if i == "y":
                a = (int(input("FID ")), input("FNAME "), int(input("AGE " )), input("SUBJECT "), int(input("SALARY ")), input("DESIGNATION ")) 
                cur.execute(f"insert into faculty values{a}")
                con.commit()
            else:
                break
    con.close()
    cur.close()
 
def show_table():
    con = mc.connect(host = "localhost", user = "root", password = "sql123", database = "institution")
    if con.is_connected():
        cur = con.cursor()
        cur.execute("select * from faculty;")
        print (f"{'FID':<20}{'FNAME':<20}{'AGE':<20}{'SUBJECT':<20}{'SALARY':<20}{'DESIGNATION':<20}")
        for i in cur:
            print (f"{i[0]:<20}{i[1]:<20}{i[2]:<20}{i[3]:<20}{i[4]:<20}{i[5]:<20}")

def update():
    con = mc.connect(host = "localhost", user = "root", password = "sql123", database = "institution")
    if con.is_connected():
        cur = con.cursor()
        n = int(input("enter salary increment %"))
        cur.execute(f"update faculty set salary = ((salary / 100)* {n} + salary);")
        con.commit()
        print ("updated data")
    cur.close()
    con.close()

def delete():
    con = mc.connect(host = "localhost", user = "root", password = "sql123", database = "institution")
    if con.is_connected():
        cur = con.cursor()
        n = int(input("enter TID to be deleted "))
        cur.execute(f"delete from faculty where TID = {n};")
        con.commit()
        print ("Data is deleted if it existed in the table ")
def search():
    con = mc.connect(host = "localhost", user = "root", password = "sql123", database = "institution")
    if con.is_connected():
        cur = con.cursor()
        n = input("enter subject to be searched ")
        cur.execute(f"select * from faculty where SUBJECT = '{n}';")
        print (f"{'FID':<20}{'FNAME':<20}{'AGE':<20}{'SUBJECT':<20}{'SALARY':<20}{'DESIGNATION':<20}")
        for i in cur:
            print (f"{i[0]:<20}{i[1]:<20}{i[2]:<20}{i[3]:<20}{i[4]:<20}{i[5]:<20}")
    cur.close()
    con.close()


while True:
    a  = input('''MENU: 
    a) Store data 
    b) show table
    c) update data with salary increment
    d) delete data
    e) search for information based on subject 
    f) any other input to exit from the menu ''')
    if a == "a":
        store()
    if a == "b":
        show_table()
    if a == "c":
        update()
    if a == "d":
        delete()
    if a == "e":
        search()
    else:
        break









 
























































































