# File: hw6_part3.py
# Author: Nana Owusu
# Date: 11/21/16
# Section: 29
# E-mail: onana1@umbc.edu
# Description: This program counts the number of ears and horns in a line of 
# horses and unicorns.

#############################################################
# count() Takes in an integer and returns the total number of 
#         ears and horns.
# Input:  length; userInput, length of the line
# Output: userTotal, total of ears and horns 
def count(length):
    if length == 0:
        return 0
    if length % 2 == 0:
        return 2 + count(length-1)
    else:
        return 3 + count(length-1)

def main():
    
    lineLength = int(input("How long is the line of equines? "))
    numParts = count(lineLength)
    print("In a line of " + str(lineLength) + ", there are " + str(numParts) + " ears and horns.")

main()
