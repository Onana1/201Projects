# File: hw5_part4.py
# Author: Nana Owusu
# Date: 10/13/17
# Section: 29
# E-mail: onana1@umbc.edu
# Description: This program ask he user to enter a number and then checks 
# different propertites of the number.

##########################################################
# checkPositive() prints if the given number
#                 is odd or even
# Input: userNum; an integer chosen by the user
# Output: None
def checkOddOrEven(numCheck):

    if numCheck % 2 == 0:
        print(numCheck, "is even")
    else:
        print(numCheck, "is odd")

##########################################################
# checkPositive() prints if the given number
#                 is positive, negative, or zero
# Input: userNum; an integer chosen by the user
# Output: None
def checkPositive(numCheck):
    
    if numCheck > 0:
        print(numCheck, "is positive")
    elif numCheck < 0:
        print(numCheck, "is negative")
    else:
        print(numCheck, "is zero")

##########################################################
# checkPositive() prints if the given number
#                 is divisible by a user inputed number
# Input: userNum; an integer chosen by the user
# Output: None
def checkDivisible(numCheck):

    numDivis = int(input("Enter number to divide by: "))
    if numCheck % numDivis == 0:
        print(numCheck, "is divisible by" , numDivis)
    else:
        print(numCheck, "is not divisible by" , numDivis)

def main():

    numCheck = int(input("Enter the number you would like to check: "))
    checkOddOrEven(numCheck)
    checkPositive(numCheck)
    checkDivisible(numCheck)

main()

