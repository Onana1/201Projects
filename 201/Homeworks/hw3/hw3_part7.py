# File: hw3_part7.py
# Author: Nana Owusu
# Date: 9/29/17
# Section: 29
# E-mail: onana1@umbc.edu
# Description: This program ask the user for a height of a triangle and what 
# character the triangle should be made up of and prints a triangle of that 
# height and character.

def main():

    triHeight = int(input("Please enter the height of your triangle:"))
    charSymbol = input("Please enter a single character for the symbol:")
    count = 0 
    charMore = 0
    
    while charMore < triHeight:
        while count <= charMore:
            print(charSymbol, end= "")
            count += 1
        charMore += 1
        count = 0
        print()
main()
