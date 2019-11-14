# File: hw4_part1.py
# Author: Nana Owusu
# Date: 10/6/17
# Section: 29
# E-mail: onana1@umbc.edu
# Description: This program ask for two integers and creates a modulus table.

def main():

    numMod = int(input("Please enter the number to mod by:"))
    numHigh = int(input("Please enter how high you'd like to go:"))
    count = 0
    
    while count <= numHigh:
        numAnswer = count % numMod
        print(count, "%" , numMod ,"=", numAnswer)
        count += 1

main()
