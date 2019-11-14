# File: hw6_part2.py
# Author: Nana Owusu
# Date: 11/21/16
# Section: 29
# E-mail: onana1@umbc.edu
# Description: This program draws a right triangle of a userInput height and 
# userInput symbol that the triangle is made up of.

#############################################################
# recurTri() prints out lines of characters to make a right
#            triangle
# Input:     height; a userInteger that is the height of the triangle
#            symbol; character that the triangle is made of 
#            line; string where the body of the triangle is printed
# Output:    None;
def recurTri(height, symbol, line):
    if height > 0:
        recurTri(height - 1,symbol, line)
        while len(line) < height: 
            line += symbol
        print(line)
        line = ""

def main():
    triHeight = int(input("Please enter the height of the triangle: "))
    triSymbol = input("Please enter the symbol to use: ")
    triLine = ""
    recurTri(triHeight, triSymbol, triLine)

main()
