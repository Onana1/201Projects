# File: food.py
# Author: Nana Owusu
# Date: 9/21/2017
# Section: 29
# E-mail: onana1@umbc.edu
# Description: This program ask the user for information on what the ate for br#eakfast and after gives a response based on what was entered.

def Main():

    foodAte = input("Please enter what you ate for breakfast:")
    
    if (foodAte == "green eggs") or (foodAte == "ham"):
        print("Excellent choice!")
    else:
        print(foodAte, "is a strange choice for breakfast.")

Main()
