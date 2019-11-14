# File: hw3_part2.py
# Author: Nana Owusu
# Date: 9/28/17
# Section: 29
# E-mail: onana1@umbc.edu
# Description: This program ask the user for two numbers and computes the
# first number to the power of the second.

def main():

    numFirst = int(input("Please enter the first number:"))
    numSecond = int(input("Please enter the second number:"))
    count = 1
    numTotal = numFirst
    
    while count < numSecond:
        numTotal *=  numFirst
        count += 1
       
    if numSecond == 0:
        numTotal = 1
    print(numFirst , "**" , numSecond , "=" , numTotal)
      
main()  
