"""
Assignment 1 Question 2 done by Vansh Aggarwal
Date: 15/3/24 
Time of start: 11:53

"""

opt1 = 0

def string_to_list(main_string, split_string,opt1):
    i=0
    req_list = []
    temp = ""
    if opt1 == 1 or opt1 ==2:
        check_num = len (split_string)
        while i <= (len(main_string)- check_num):
            if main_string [i] == split_string[0]:
                main_string[i: (i+check_num+1)] == split_string
                req_list.append(temp) 
                temp =""
                i+=check_num


            elif main_string [i] != split_string[0]:
                temp += main_string[i]
                i+=1
        req_list.append(temp) 
        


    elif opt1 == 3:
        for i in main_string:
            if i != " ":
                temp += i
            elif i == " " and temp != "" and temp != " ":
                req_list.append(temp)
                temp = ""


    return (req_list)



while opt1 != 4:
    main_string = input ("Enter Main String: ")

    print(''' 
    1. split string value is a substring
    2. split string value is space
    3. split string value is not given.
    4. exit.
    ''')
    opt1 = int(input("Enter option number: "))

    if opt1==1:
        split_string = input ("Enter the split string: ")
    elif opt1 ==2:
        split_string = " "

    elif opt1 ==3:
        split_string = " "
    
    elif opt1 == 4:
        break
    
    else:
        print ("input not recognised")
        break 

    print (string_to_list (main_string, split_string,opt1))


