# File: hw4_part7.py
# Author: Nana Owusu
# Date: 10/6/17
# Section: 29
# E-mail: onana1@umbc.edu
# Description: This program allows the user to create a task list that reminds
# them of the task and the hours left to complete it.

SENTINEL = "STOP"

def main():

    groceryBox = []
    countOne = 0
    countTwo = 0
    countThree = 0
    typeGrocery = input("Please enter a grocery item, or 'STOP' to exit:")

    while typeGrocery != SENTINEL:
        groceryBox.append(typeGrocery)
        typeGrocery = input("Please enter a grocery item, or 'STOP' to exit:")
        while countThree < len(groceryBox):
            if typeGrocery == groceryBox[countThree]:
                print("Error: The item", typeGrocery, "is already in the list")
            countThree += 1
        countThree = 0
        countOne += 1
    print("There are", len(groceryBox) , "groceries in your list:")
    while countTwo < countOne:
        print(groceryBox[countTwo])
        countTwo += 1
main()
