# File: hw3_part3.py
# Author: Nana Owusu
# Date: 9/28/17
# Section: 29
# E-mail: onana1@umbc.edu
# Description: This program has the user input the time by entering the hours,
# minutes and time period then prints out the time.

def main():

    print("Please enter the time: hours, then minutes, then AM/PM")
    
    numHours = int(input("Please enter the hour:"))
    while numHours <  1 or numHours > 12:
        if numHours < 1:
            print("The hours value is too low")
            numHours = int(input("Please enter the hour:"))
        elif numHours > 12:
            print("The hours value is too high")
            numHours = int(input("Please enter the hour:"))
       
    numMinute = int(input("Please enter the minute:"))
    while numMinute < 0 or numMinute > 59:
        if numMinute < 0:
            print("The minutes value is too low")
            numMinute = int(input("Please enter the minute:"))
        elif numMinute > 59:
            print("The minutes value is too high")
            numMinute = int(input("Please enter the minute:"))
    
    timePeriod = input("Please enter the time period:")
    while timePeriod != "AM" and  timePeriod != "PM":
        print("Time period must be 'AM' or 'PM'.")
        timePeriod = input("Please enter the time period:")
    print("It is" , numHours , ":" , numMinute , timePeriod)
            
main()

