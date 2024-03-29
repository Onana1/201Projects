# File: hw5_part1.py
# Author: Nana Owusu
# Date: 10/13/17
# Section: 29
# E-mail: onana1@umbc.edu
# Description: This program ask the user for a string and a letter and counts
# how many times the letter appears in the string.

###########################################################
# numLetter() counts the instances of a letter in a string
# Input: aString; a string of the phrase to search in
# letter; a single character to search for
# Output: None
def numLetter(theList):
    askLetter = input("Enter a letter to search for: ")
    askLetterLow = askLetter.lower()
    count = 0
    numAmount = 0
    while count < len(theList):
        if theList[count] == askLetterLow:
            numAmount += 1
        count +=1
    print("There are", numAmount, "instances of", askLetter, "in the String")


def main():
    askString = []
    askString = input("Enter a string: ")
    askString = askString.lower()
    numLetter(askString)
    
main()
