# File: hw2_part1.py
# Author: Nana Owusu
# Date: 9/22/2017 
# Section: 29
# E-mail: onana1@umbc.edu
# Description: This prorgam ask the user for information about how long they wa#aited to start on a design and how long tbey waited to start on a project.

def main():

    print("Project 1 has just come out, and you have 6 days to complete the design, and 13 days to complete the project.")

    numDesign = int(input("Days left when you start the design:"))
    numProject = int(input("Days left when you start the project:"))

    if (numDesign == 0) or (numProject == 0):
        print("Why would you wait so long!? :(")
    elif (numDesign == 6) and (numProject >=10) and (numProject <=13):
        print("Wow, you started really early! Good Job! :)")
    else:
        print("Good luck on the project! You can do it!")

main()
