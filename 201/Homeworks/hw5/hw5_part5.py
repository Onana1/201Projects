# File: hw5_part5.py
# Author: Nana Owusu
# Date: 10/13/17
# Section: 29
# E-mail: onana1@umbc.edu
# Description: This program ask the user to enter a series of strings and prints
# out the strings in reverse.

######################################################
# backwards() reverses a string and prints the result
# Input: forString, a string to reverse
# Output: None
def backwards(theList):
    count1 = 0
    count2 = 0
    changeWord = []
    print(theList)
    while count1 < len(theList):
        changeWord = theList[count1]
        print(theList)
        while count2 < len(changeWord):
            changeWord[count2] = changeWord[len(changeWord)-count2]
            count2 += 1
        print(theList[count1])
        print("The string", theList[count1], "reversed is", changeWord)
        count1 += 1
        count2 = 0
        
def main():
    
    wordBox = []
    wordNum = int(input("How many words would you like to turn backwards: "))
    count = 1
    
    while count <= wordNum:
        wordBack = input("Please enter string #" + str(count) + ":")
        wordBox.append(wordBack)
        count += 1
    print(wordBox)
    backwards(wordBox)

main()
