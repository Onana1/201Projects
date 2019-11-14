#File: hw_part1.py
#Author: Nana Owusu
#Date: 9/14/17
#Section: 29
#E-mail: onana1@umbc.edu
#Description: This program prints out the total amount of dogs, cats or fish th#at you have as pets.

def main():

    numDogs = int(input("How many dogs do you have?:"))
    numCats = int(input("How many cats do you have?:"))
    numFish = int(input("How many fish do you have?:"))

    Total = numDogs + numCats + numFish

    print("You have" ,numDogs, "dogs as pets.")
    print("You have" ,numCats, "cats as pets.")
    print("You have" ,numFish, "fish as pets.")

    print("You have a total of" , Total , "pets.")

main()
