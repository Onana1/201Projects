# File: hw5_part3.py
# Author: Nana Owusu
# Date: 10/13/17
# Section: 29
# E-mail: onana1@umbc.edu
# Description: This program checks the grammar of a sentence and tells you what
# is wrong with your sentence.

SENTINEL = ""

###########################################################
# checkCapital() checks the to see if starting letter is capitalized
# Input: aString; string of phrases or a complete sentence
# Output: None
def checkCapital(theList):

    count = 0
    
    if theList[count] != theList[count].upper():
        print("Wrong - Sentences start with a capital letter.")
    elif theList[count] == theList[count].upper():
        print("Correct capitalization!")
        
###########################################################
# checkPunctuation() checks the to see if the string has an ending punctuation
# Input: aString; string of phrases or a complete sentence
# Output: None
def checkPunctuation(theList):
    
    pCount = len(theList) - 1
    
    if theList[pCount] != "?" and theList[pCount] != "!" and theList[pCount] != ".":
        print("Wrong - Sentences use punctuation.")
    else:
        print("Correct punctuation!")

def main():
    
    askSent = []
    askSent = input("Enter a sentence (enter nothing to quit): ")
    
    while askSent != SENTINEL:
        checkCapital(askSent)
        checkPunctuation(askSent)
        askSent = input("Enter a sentence (enter nothing to quit): ")

main()
