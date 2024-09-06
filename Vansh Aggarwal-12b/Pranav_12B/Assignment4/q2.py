"""PRANAV PRADEEP
ASSIGNMENT 4: Q 5: 26/6/24"""

def add_dict(dict):
    dict[input("Enter Registration No:")] = int(input("Enter Marks: "))

def update_stack(stack, dict):
    for keys in dict:
        for i in stack:
            if i[0] == keys:
                break
        else:
            if len(stack) >= 7:
                print("Stack overflow ")
            elif dict[keys] > 98.5:
                stack.append((keys, dict[keys]))

def project(stk):
    l = []
    if len(stk) == 0:
        print("stack empty ")
    else:
        print (f'{"Registration No":30}{"Marks":30}')
        for i in range (len(stk)-1,-1,-1):
            q = stk.pop()
            print (f'{q[0]}{q[1]:30}')
            l.append(q)

        for j in range (len(l)-1,-1,-1):
            stk.append(l.pop())

def search(stk):
    l = []
    check = 0
    if len(stk) == 0:
        print("stack empty ")
    else:
        p = input("enter registration number of student to be searched for: ")
        print (f'{"Registration No ":30}{"Marks":30}')
        for i in range (len(stk)-1,-1,-1):
            q = stk.pop()
            if q[0] == p:
                print (f'{q[0]:30}{q[1]}')
                check = 1
            l.append(q)
        if check == 0:
            print ("Sorry the candidate was not accepted ")

        for j in range (len(l)-1,-1,-1):
            stk.append(l.pop())

def withdraw(stk):
    l = []
    check = 0
    if len(stk) == 0:
        print("stack empty ")
    else:
        p = input("enter registration number of student to be searched for: ")
        print (f'{"Marks ":30}{"Registration No":30}')
        for i in range (len(stk)-1,-1,-1):
            q = stk.pop()
            if q[0] == p:
                check = 1
                print("Candidate admission has been withdrawn ")
            else:
                l.append(q)
        if check == 0:
            print ("Sorry the candidate data could not be retrieved ")

        for j in range (len(l)-1,-1,-1):
            stk.append(l.pop())


stk = []    
d = {"121100":100, "4279":70, "363636":244}
while True:
    a = input('''Enter what you want to do: 
1) Add elements to dictionary
2) Update Stack
3) Display selection list
4) Search for candidate result in stack
5) Withdraw the admission from stack
6) EXIT
''')
    if a == "1":
        add_dict(d)
    if a == "2":
        update_stack(stk, d)
    if a == "3":
        project(stk)
    if a == "4":
        search(stk)
    if a == "5":
        withdraw(stk)
    if a == "6":
        break