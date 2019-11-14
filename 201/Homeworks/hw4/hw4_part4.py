# File: hw4_part4.py
# Author: Nana Owusu
# Date: 10/6/17
# Section: 29
# E-mail: onana1@umbc.edu
# Description:This program ask the user about the test they have taken and if
# they had extra credit and prints it out.

def main():

    numTest = int(input("Enter number of test taken:"))
    count = 1
    numHighest = 0
    
    while count <= numTest:
        print("For Test #", count, "was extra credit allowed?")
        typeChoice = input("Please enter 'yes' or 'no':")
        if typeChoice == "no":
            numGrade = int(input("Please enter your grade for the test:"))
            while numGrade < 0 or numGrade > 100:
                if numGrade > 100:
                    print("Test grade must be between 0 and 100")
                elif numGrade < 0:
                    print("Test grade cannot be negative")
                numGrade = int(input("Please enter your grade for the test:"))
        elif typeChoice == "yes":
            numGrade = int(input("Please enter your grade for the test:"))
            while numGrade < 0:
                print("Test grade cannot be negative")
                numGrade = int(input("Please enter your grade for the test:"))
        if numGrade > numHighest:
            numHighest = numGrade
        count += 1
    print("The highest grade received was" ,numHighest)
    
main()    

        
