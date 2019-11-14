# File: hw1_part2.py
# Author: Nana Owusu
# Date: 9/14/17
# Section: 29
# E-mail: onana1@umbc.edu
# Description: This program ask for the amount of a bill and the amount of how #many people are in your party, then calculates the amount each person pays.

def main():
    
    numBill = float(input("How much was the total bill?:"))
    numPeople = int(input("How many people are in your party?:"))
    numCostPer = numBill/numPeople

    print("Each person needs to pay $" ,numCostPer)

main()    
