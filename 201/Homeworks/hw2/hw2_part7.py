# File: hw2_part7.py
# Author: Nana Owusu
# Date: 9/22/2017
# Section: 29
# E-mail: onana1@umbc.edu
# Description: This prorgam ask the user for about two swtiches and use the 
# information gained to determine the state of the  generator.

def main():
    
    print("Please enter 'y' for yes and 'n' for no.")
    
    genF = input("Is the first switch on? (y/n)")
    genS = input("Is the second switch on? (y/n)")

    if genF == "y" and genS == "y" or genF == "n" and genS == "n":
        print("The generator is off.")
    else:
        print("The generator is on.")

main()
