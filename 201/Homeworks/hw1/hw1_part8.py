# File: hw1_part8.py
# Author: Nana Owusu
# Date: 9/15/17
# Section: 29
# E-mail: onana1@umbc.edu
# Description: This program ask the user how many items of food they want to bu#y based on a fixed price and calculates and prints the total cost.

def main():

    costApp = 9.5
    costMainDish = 15.8
    costDesserts = 6.55
    
    print("Appetizers cost" ,costApp,)
    numApp = int(input("How many appetizers would you like to order?:"))
    print("Main dishes cost" ,costMainDish,)
    numMainDish = int(input("How many main dishes would you like to order?:"))
    print("Desserts cost" ,costDesserts,)
    numDesserts = int(input("How many desserts would you like to order?:"))
    
    totalApp = costApp * numApp
    totalMainDish = costMainDish * numMainDish
    totalDesserts = costDesserts * numDesserts

    totalCost = totalApp + totalMainDish + totalDesserts

    print("The total cost of your meal will be" ,totalCost,)

main()
