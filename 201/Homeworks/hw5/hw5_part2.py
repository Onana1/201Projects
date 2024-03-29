# File: hw5_part2.py
# Author: Nana Owusu
# Date: 10/13/17
# Section: 29
# E-mail: onana1@umbc.edu
# Description: This program ask the user for a string and a word to search for
# and each time the word is found the program prints the index of where it was
# found.

########################################################
# inPhrase() takes in the string and looks for a certain word
# Input: str; a set of strings or a sentence
# Output: none
def inPhrase(theList):
    askWord = []
    askWord = input("Please enter a word to search for: ")
    askWordLow = askWord.lower()
    count = 0
    countWord = 0
    numAmount = 0
    numIndex = 0
    while count < len(theList):
        while theList[count] == askWordLow[countWord]:
            while countWord < len(askWordLow):
                countWord += 1
                count += 1
        while theList[count] != askWordLow[countWord]:
                count += 1
                
        numIndex = count - count
        numAmount += 1          
        countWord = 0
        print("Found" ,askWord, "low at index" , numIndex) 
    print("Found", askWord, "a total of", numAmount, "times")


def main():
    askPhrase = []
    askPhrase = input("Please enter a phrase: ")
    askPhrase = askPhrase.lower()
    inPhrase(askPhrase)

main()
