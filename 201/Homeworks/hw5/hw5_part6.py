# File: hw5_part6.py
# Author: Nana Owusu
# Date: 10/13/17
# Section: 29
# E-mail: onana1@umbc.edu
# Description: This program allows the user to enter a list of temperatures and 
# calls an average function that will return average the numbers.

SENTINEL = "STOP"
########################################################
# average() calculates and returns the average
# Input: numList; a list of floats
# Output: avgNum; a float, average of list's numbers
def average(theList):
    numTotal = 0
    numAverage = 0
    count = 0
    while count < len(theList):
        numTotal += theList[count]
        count += 1
    numAverage = numTotal/len(theList)
    return numAverage
        
def main():
    
    tempBox = []
    numTemp = input("Enter a temperature, 'STOP' to exit: ")
    while numTemp != SENTINEL:
        tempBox.append(float(numTemp))
        numTemp = input("Enter a temperature, 'STOP' to exit: ")
    theAverage = average(tempBox)
    print("The average is", theAverage)

main()
