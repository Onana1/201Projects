# File: hw2_part2.py
# Author: Nana Owusu
# Date: 9/22/2017
# Section: 29
# E-mail: onana1@umbc.edu
# Description: This prorgam ask the user for a number and whether they want to
# round the number up or down.

def main():

    numNumber = float(input("Input the number you are rounding:"))
    choiceRound = input("Do you want to round up or down?:")
    
    numUp = int((numNumber + 1) // 1)
    numDown = int(numNumber // 1)
    print("Original value:" ,numNumber)

    if choiceRound == "up":
        print("Rounded value:" , numUp)
    elif choiceRound == "down":
        print("Rounded value:" , numDown)
    else:
        print("Rounded value:" , numNumber)

main()

