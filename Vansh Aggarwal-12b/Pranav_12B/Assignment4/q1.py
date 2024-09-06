"""PRANAV PRADEEP
ASSIGNMENT 4: Q 3: 26/6/24"""

def push(stk):
    t = (input("Magname: "), input("Type: "),input("Frequency: "), int(input("Price: ")))
    stk.append(t)
    print ("element pushed ")

def pop(stk):
    if len(stk) == 0:
        print("underflow ")
    else:
        print(stk.pop())

def peek(stk):
    if len(stk) == 0:
        print("Stack is empty ")
    else:
        print("The top element is ", stk[-1][0],stk[-1][1],stk[-1][2],stk[-1][3])

def project(stk):
    l = []
    if len(stk) == 0:
        print("stack empty ")
    else:
        print (f'{"Mag Name":30}{"Type":30}{"Frequency":30}{"Price":30}')
        for i in range (len(stk)-1,-1,-1):
            q = stk.pop()
            print (f'{q[0]:30}{q[1]:30}{q[2]:30}{q[3]}')
            l.append(q)

        for j in range (len(l)-1,-1,-1):
            stk.append(l.pop())

mag = [("Times Magazine", "Business", "Monthly", 500), ("Bangalore Magazine", "Fashion", "Bi-Monthly", 400) ]
while True:
    a = input('''Enter what you want to do: 
1) Push
2) Pop
3) Peek
4) Project
5) Exit
''')
    if a == "1":
        push(mag)
    if a == "2":
        pop(mag)
    if a == "3":
        peek(mag)
    if a == "4":
        project(mag)
    else:
        break

