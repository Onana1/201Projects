# File: hw3_part5.py
# Author: Nana Owusu
# Date: 9/29/17
# Section: 29
# E-mail: onana1@umbc.edu
# Description: This program prints out 1 to 77 and in three speacial cases
# instead of a number being printed a phrase is printed in its place.

def main():
    numStart = 1

    while numStart >= 1 and numStart <= 77:
        if numStart % 5 == 0 and numStart % 4 == 0:
            print("The year 2020 coming soon!")
            numStart += 1
        elif numStart % 4 == 0:
            print("Four leaf clovers are lucky!")
            numStart += 1
        elif numStart % 5 == 0:
            print("Where do yo usee yourself in five years?")
            numStart += 1
        else:
            print(numStart)
            numStart += 1
            
main()
