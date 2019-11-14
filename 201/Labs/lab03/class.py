# File: class.py
# Author: Nana Owusu
# Date: 9/21/2017
# Section: 29
# E-mail: onana1@umbc.edu
# Description: This program ask the user for their professor's name and if it i#is Neary or Gibson if ask for hte number of students in their class.

def Main():

    whoTeacher = input("Enter you professor's name:")

    if (whoTeacher == "Gibson") or (whoTeacher == "Neary"):
        numClass = int(input("How many students are in your class?:"))
        if numClass >= 80:
            print("Wow so many options for study groups!")
        elif (numClass < 80) and  (numClass > 30):
            print("You have so many chances to make new friends!")
        else:
            print("You'll get to know all your classmates really well! :)")
    else:
        print(whoTeacher, "does not teach CMSC 201! You're in the wrong class!")

Main()

        
