# File: hw1_part7.py
# Author: Nana Owusu
# Date: 9/15/17
# Section: 29
# E-mail: onana1@umbc.edu
# Description: This program ask the user for ratings on a resturant and prints #out a summary of their experience.

def main():

    foodRating = float(input("How would you rate the food? (1-5):"))
    servRating = float(input("How would you rate the service? (1-5):"))
    atmoRating = float(input("How would you rate the atmosphere? (1-5):"))
    
    overallRating =(foodRating + servRating + atmoRating)/3

    print("Your overall experience was" ,overallRating, "stars")

main()
