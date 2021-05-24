# Import needed Library
import os

def Main():

    Directory = input("Please enter the file directory you would like your file saved to (pst, its farquad.txt) : ")
    File = input("Please enter the name you wish to grant your file: ")
    Name = input("Please enter your name: ")
    Address = input("Please enter your Address: ")
    PhoneNumber = input("Please input your phone number: ")

# Directory Validation (does the path exist?) 
    if os.path.isdir(Directory):
        WriteFile = open(os.path.join(Directory, File), "w")
        WriteFile.write(Name+ "," +Address+ "," +PhoneNumber+ "/n")
        WriteFile.close()

        print("File: ")
        ReadFile = open(os.path.join(Directory, File), "r")
        for line in ReadFile:
            print(line)
        ReadFile.close()
    else:
        print("There was an error in finding that file path, please try again.")



Main()

