# File: hw6_part1.py
# Author: Nana Owusu
# Date: 11/21/16
# Section: 29
# E-mail: onana1@umbc.edu
# Description: This program calculates the summation of a number and stops at a
# second number that is userInput.


#############################################################
# numSummation() calculates the summation of a number and
#                returns an integer
# Input:         num; userInteger as the starting number
#                base; userInteger as teh stopping number
# Output:        userInteger; returns the sum of the summation
def numSummation(num,base):
    if num == base:
        return base
    else:
        return num + numSummation(num-1,base)
def main():

    numFrom = int(input("Please input the number you want to sum from: "))
    numDown = int(input("Please input the number you want to sum down to: "))
    
    sumNum = numSummation(numFrom,numDown)
    print("The summation from " + str(numFrom) + " to " + str(numDown) + " is "+  str(sumNum))
    
main()
