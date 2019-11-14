# File: hw3_part1.py
# Author: Nana Owusu
# Date: 9/28/17
# Section: 29
# E-mail: onana1@umbc.edu
# Description: This program ask the user for the starting hailstone size and 
# simulates the up and down movement of a hailstone in a storm.

def main():
    
    numHail = int(input("Please enter the starting height of the hailstone:"))
    numEven = numHail // 2
    numOdd = (numHail * 3) + 1
    
    while numHail > 1:
       print("Hail is currently at height", numHail)
       if numHail % 2 == 0:
            numHail = numHail // 2
       elif numHail % 2 != 0:
            numHail = (numHail * 3) + 1
    print("Hail stopped at height", numHail)

main()
            
