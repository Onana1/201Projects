# File: hw1_part4.py
# Author: Nana Owusu
# Date: 9/15/17
# Section: 29
# E-mail: onana1@umbc.edu
# Description: This program ask for information about a car being bought and pr#int out the total cost of the car.

def main():
    
    carCost = float(input("How much does the car cost?:"))
    carWarranty = float(input("How much does the warranty cost?:"))
    carFees = float(input("How much are the fees?:"))
    carTaxes = float(input("How much are the taxes?:"))

    carTotal = carCost + carWarranty + carFees + carTaxes

    print("The total cost of the car will be" ,carTotal,)

main()
