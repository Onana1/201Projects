# File: hw3_part4.py
# Author: Nana Owusu
# Date: 9/29/17
# Section: 29
# E-mail: onana1@umbc.edu
# Description: This program calculates how much money is raised in a charity 
# run by asking for the amount of pledges, then miles covered and outputs
# the donation amount made.

def main():

    numPledged = int(input("How many pledges did you secure?"))
    count = 1
    numTotal = 0

    while numPledged >= count:
        print("For pledge #", count)
        numMoney = float(input("How much money was pledged?"))
        numTotal = numTotal + numMoney
        count += 1
    numMiles = int(input("How many miles did you run for charity?"))
    numEarned = numMiles * numTotal
    print("Based on your" , numMiles , "miles you earned $" , numEarned, "for the charity.")

main()

        
