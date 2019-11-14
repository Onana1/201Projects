# File: hw4_part3.py
# Author: Nana Owusu
# Date: 10/6/17
# Section: 29
# E-mail: onana1@umbc.edu
# Description: This program has the user enter a list of names of students in 
# a course and prints out the amount of students in the course.

SENTINEL = "QUIT"

def main():

    nameBox = []

    nameStudent = input("Please enter a student name (QUIT to stop):")
    while len(nameBox) <= 6 and nameStudent != SENTINEL:
        nameBox.append(nameStudent)
        nameStudent = input("Please enter a student name (QUIT to stop):")
    if len(nameBox) == 7:
        print("There are" , len(nameBox) + 1, "students in the course")
        print("The course is perfectly enrolled!")
    elif len(nameBox) < 7:
        print("There are" , len(nameBox) + 1, "students in the course!")
        print("The course is under enrolled!")

main()
    
