# File: hw1_part5.py
# Author: Nana Owusu
# Date: 9/15/17
# Section: 29
# E-mail: onana1@umbc.edu
# Description: This program ask for inforamtion about a restaurant and prints o#ut that inforamtion.

def main():
    
    nameInfo = input("What is the restaurant's name?:")
    foodInfo = input("What type of food does the restaurant serve?:")
    ratingInfo = int(input("What is the restaurant's star rating?:"))
    
    print(nameInfo, "is a" ,ratingInfo, "star restaurant, serving" ,foodInfo, "food")

main()
