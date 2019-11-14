# File: hw2_part3.py
# Author: Nana Owusu
# Date: 9/22/2017
# Section: 29
# E-mail: onana1@umbc.edu
# Description: This prorgam simulates a deli order and ask the user for their 
# type of sandwich, side, and drink, and informs them of the order.

def main():

    print("Welcome to the CMSC 201 deli")

    print("Pick 'ham', 'cheese', or 'veggie' for your sandwich")
    choiceSand = input("Choose a sandwich:")
    
    print("Pick 'cookies', 'chips', or pickle for your side")
    choiSide = input("Choose a side:")

    print("Pick 'water', lemonade', or 'soda' for your drink")
    choiDrink = input("Choose a drink:")

    if choiceSand == "ham" or choiceSand == "cheese" or choiceSand == "veggie":
        print("You chose a" ,choiceSand, "sandwich.")
    else:
        print("A" ,choiceSand, "is not a proper choice for a sandwich.")
    if choiSide == "cookies" or choiSide == "chips" or choiSide == "pickle":
        print("You chose a" , choiSide, "for your side.")
    else:
        print("A" ,choiSide, "is not a proper choice for a side.")
    if choiDrink == "water" or choiDrink == "lemonade" or choiDrink == "soda":
        print("You chose a" ,choiDrink, "for your drink.")
    else:
        print("A" ,choiceDrink, "is not a proper choice for a drink.")

    print("Enjoy you meal")

main()
