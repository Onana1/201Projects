# File: hw1_part6.py
# Author: Nana Owusu
# Date: 9/15/17
# Section: 29
# E-mail: onana1@umbc.edu
# Description: This program ask for information about a bill and calculates the#total amount to pay.

def main():

    costBill = float(input("How much was the bill?:"))
    taxPercent = float(input("How much is tax in your area?:"))
    tipPercent = float(input("What percentage do you want to tip?:"))
    
    numTax = taxPercent/100
    numTip = tipPercent/100
    numTotal = costBill + (costBill*numTax) + (costBill*numTip)

    print("The total cost of the meal will be" ,numTotal,)

main()


