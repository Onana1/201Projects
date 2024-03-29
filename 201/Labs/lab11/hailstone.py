# File:    hailstone.py
# Started: by Dr. Gibson
# Author:  Nana Owusu
# Date:    11/16/17
# Section: 29
# E-mail:  onana1@umbc.edu
# Description:
#   This file contains python code that implements the
#   "flight" of a hailstone, following the HOTPO rules
#   (also known as the Collatz Conjecture), recursively

# NO CONSTANTS NEEDED, THE NUMBERS USED IN flight() ARE
#    PART OF A FORMULA/MATHEMATICAL CONJECTURE

############################################################
# flight() recursively calculates the path of a hailstone
# Input:   the height of the hailstone
# Output:  a recursive call, which at the end returns 
#          the number of "steps" taken for the
#          hailstone to reach a height of 1
def flight(height):
    print("Height of", height)
    steps = 0 
    #### BASE CASES:
    # print out an "invalid" message and return 0
    if height < 0:
        print("Invalid height of", height)
        return 0
    # stops when it reachs height of 1 (the ground)
    if height == 1:
        return steps
    #### RECURSIVE CASES:
    # if the current height is even, divide it by 2
    else:
        if height % 2 == 0:
            steps += 1
            return steps + flight(height//2)
    # if the current height is odd, multiply it by 3, then add 1
        if height % 2 != 0:
            steps += 1
            return steps + flight(height*3 + 1)

def main():

    print("Welcome to the Hailstone Simulator!")
    msg = "Please enter a height for the hailstone to start at: "
    startHeight = int(input(msg))

    steps = flight(startHeight)

    print("\nIt took", steps, "steps to hit the ground.")

    print("Thank you for using the Hailstone Simulator!\n")

main()

    

