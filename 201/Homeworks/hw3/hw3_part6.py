# File: hw3_part6.py
# Author: Nana Owusu
# Date: 9/29/17
# Section: 29
# E-mail: onana1@umbc.edu
# Description: This program ask the user for the width and height of a box 
# and prints out the box using numbers.

def main():

    numWidth = int(input("Please enter a width:"))
    numHeight = int(input("Please enter a height:"))
    count = 0
    numUp = 1
    
    while numUp <= numHeight:
        while count < numWidth * numUp:
            count += 1
            print(count , end= " ")
        print()
        numUp += 1

            
main()
        


