"""
Assignment 3 Question 1 done by Vansh Aggarwal
Date: 18/6/24 
Time of start: 11:30

"""
import pickle as p

#create file

def create_file():
    f = open("movie.dat", "wb")
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

def addmovie():
    rating = 1000
    while rating<0 or rating > 10:
        rating = int(input("Enter the movie rating: "))

    movie = input ("Enter movie name: ")
    language = input ("Enter movie language: ")

    fout = open("movie.dat", "ab")
    temp_input = [rating, movie, language]
    p.dump(temp_input, fout)
    fout.close()

def readmovie():
  data = []
  try:
    with open("movie.dat", "rb") as fout: 
      while True:
        data_1 = p.load(fout)
        data.append(data_1)
  except EOFError:
    print("End of file reached in 'movie.dat'.")
  finally:
    fout.close() 
    return(data)

def bestrated():
    movie = ""
    rating = 0
    data = readmovie()
    for i in data:
        if i[0]>rating:
            movie = i
            rating = i[0]
    return(movie)

        




#Main Loop: 

while True: 
    print (''' 
Options: 
1) Write the Movie to a binary file.
2) Read the Movie from a binary file and display the records.
3) Search the record of the Movie which has the highest rating. ''' )

    opt1 = int(input("Enter the option to execute: "))

    if opt1==1:
        addmovie()
    
    if opt1 ==2:
        data = readmovie()
        for i in data:
            print (i)

    if opt1 ==3:
        mov = bestrated()
        print (mov)
