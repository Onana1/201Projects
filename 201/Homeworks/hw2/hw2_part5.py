# File: hw2_part5.py
# Author: Nana Owusu
# Date: 9/22/2017
# Section: 29
# E-mail: onana1@umbc.edu
# Description: This prorgam ask the user for characteristics of a dog and 
# prints out the bread based on yes or no answers.

def main():

    print("Please enter 'yes' or 'no' to these questions.")
    
    charTail = input("Does your dog have a curly tail?")
    if charTail == "yes":
        charBark = input("Does your dog bark?")
        if charBark == "yes":
            print("Your dog is a Eurasier")
        else: 
                print("Your dog is a Basenji")
    elif charTail == "no":
            charStick = input("Does your dogs ears stick up?")
            if charStick == "yes":
                print("Your dog is a Pharoah Hound")
            elif charStick == "no":
                charColor = input("Does your dog come in multiple colors?")
                if charColor == "yes":
                    print("Your dog is a Chesapeake Bay Retriever")
                else:
                    print("Your dog is a Maremma Sheepdog")

main()
