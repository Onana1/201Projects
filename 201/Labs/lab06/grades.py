# File:        grades.py
# Started:     by Brianna Richardson (& Dr. Gibson)
# Author:      Nana Owusu
# Date:        10/12/2017
# Section:     29
# E-mail:      onana1@umbc.edu
# Description: This file contains python code that uses functions to allow 
#              a user to get information about a list of grades entered.

MIN_VAL = 0
MAX_VAL = 100
SENTINEL = -1

###################################################################
# printList() prints out a list, showing the index of each element
# Input:      theList; a list of any types of variables
# Output:     None
def printList(theList):
    #---------------------------------------------------------#
    count = 0
    while count < len(theList):
        print("At index", count , "there is", theList[count])
        count += 1
    #---------------------------------------------------------#
    

###########################################################
# printMin() prints the minimum value in a list of numbers
# Input:     theList; a list of integers and/or floats
# Output:    None
def printMin(theList):
    #-------------------------------------------------------#
    theCount = 0
    numMin = theList[0]
    while theCount <  len(theList):
        if theList[theCount] < numMin:
            numMin = theList[theCount]
        theCount += 1
    print("The minimum is", numMin)
    #-------------------------------------------------------#


###########################################################
# printMax() prints the maximum value in a list of numbers
# Input:     theList; a list of integers and/or floats
# Output:    None
def printMax(theList):
    #-------------------------------------------------------#
    theCount1 = 0
    numMax = theList[0]
    while theCount1 < len(theList):
        if theList[theCount1] > numMax:
            numMax = theList[theCount1]
        theCount1 += 1
    print("The maximum is", numMax)
    #-------------------------------------------------------#


def main():
    gradeList = []
    msg = "Enter a grade (" + str(SENTINEL) + " to quit): "

    grade = int(input(msg))

    # ask the user for grades until they choose to exit
    while(grade != SENTINEL):
        # check beforehand, so we only save valid grades
        if grade >= MIN_VAL and grade <= MAX_VAL:
            gradeList.append(grade)
        else:
            print("\tThe grade", grade, "is invalid")
            print("\tGrades must be between", MIN_VAL, "and", MAX_VAL)

        grade = int(input(msg))

    # call the print function
    #------------------------------------------------------#
    printList(gradeList)
    #------------------------------------------------------#

    # print out the minimum and maximum values
    #-------------------------------------#
    printMin(gradeList)
    printMax(gradeList)
    #-------------------------------------#

main()
