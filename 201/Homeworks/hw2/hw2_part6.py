# File: hw2_part6.py
# Author: Nana Owusu
# Date: 9/22/2017
# Section: 29
# E-mail: onana1@umbc.edu
# Description: This prorgam ask the user for the say of the month and returns 
# the day of the week.

def main():

    dayMonth = int(input("Please enter the day of the month:"))

    typeDay = int(dayMonth % 8)

    if dayMonth >= 1 and dayMonth <=30:
        if typeDay == 1:
            print("Today is Friday")
        elif typeDay == 2:
            print("Today is Saturday")
        elif typeDay == 3:
            print("Today is Sunday")
        elif typeDay == 4:
            print("Today is Monday")
        elif typeDay == 5:
            print("Today is Tuesday")
        elif typeDay == 6:
            print("Today is Wednesday")
        elif typeDay == 7:
            print("Today is Thursday")
    else:
        print("The date" ,dayMonth, "is an invalid day")

main()
        


    
