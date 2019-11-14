# File: hw4_part2.py
# Author: Nana Owusu
# Date: 10/6/17
# Section: 29
# E-mail: onana1@umbc.edu
# Description: This program ask the user for inputs in or to draw a box with
# a specific filling an outer.

def main():

    numWidth = int(input("Please enter the width of the box:"))
    numHeight = int(input("Please enter the height of the box:"))
    boxSymbol = input("Please enter a symbol for the box outline:")
    fillSymbol = input("Please enter a symbol for the box fill:")
    count = 0
    charMore = 0

    while charMore < numHeight - numHeight + 1:
        while count < numWidth:
            print(boxSymbol , end ="")
            count += 1
        print()
        count = 0
        charMore += 1
    while charMore < numHeight - 1:
        print(boxSymbol, end ="")
        while count < numWidth - 2:
            print(fillSymbol, end ="")
            count += 1
        print(boxSymbol, end ="")
        print()
        count = 0
        charMore += 1
    while charMore < numHeight:
        while count < numWidth:
            print(boxSymbol, end ="")
            count += 1
        print()
        charMore += 1
    
        

main()
            
        
