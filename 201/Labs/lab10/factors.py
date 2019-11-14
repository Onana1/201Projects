# File: factors.py
# Author: Nana Owusu
# Date: 11/9/2017
# Section: 29
# E-mail: onana1@umbc.edu
# Description: This program gets a userInput number and finds that factors of
# that number.

def main():

    posNum = int(input("Enter a (positive) number to find the factors of:"))
    
    while posNum <= 0:
        posNum = int(input("Sorry, enter a number greater than 0:"))
        
    factorBox = []
    for i in range(1,posNum + 1,1):
        factorBox.append(i)
    
    realFactorBox = []
    for j in range(len(factorBox)):
        if posNum % factorBox[j]  == 0:
            realFactorBox.append(j)
            print(str(factorBox[j]) + " is a factor of " + str(posNum)) 
        
        
main()
