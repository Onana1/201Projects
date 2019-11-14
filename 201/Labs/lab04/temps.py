# File: temps.py
# Author: Nana Owusu
# Date: 2/28/2017
# Section: 29
# E-mail: onana1@umbc.edu
# Description: YOUR DESCRIPTION GOES HERE AND HERE
# YOUR DESCRIPTION CONTINUED SOME MORE

def main():

    numTemp = float(input("How many temperatures would you like to enter?"))
    count = 0
    
    while numTemp < 1:
        print("You must enter a number greater than zero.")
        numTemp = float(input("How many temperatures would you like to enter?"))
    
        firstTemp = float(input("Enter a teamperature:"))
    while count < numTemp:
        enterTemp = float(input("Enter a teamperature:"))
        if enterTemp < firstTemp:
            numMax = 
        elif enterTemp > firstTemp:
            
        count += 1
    if count == numTemp:
        print("")
    
        
main()
