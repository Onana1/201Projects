# File: hw4_part6.py
# Author: Nana Owusu
# Date: 10/6/17
# Section: 29
# E-mail: onana1@umbc.edu
# Description: This program allows the user to create a task list that reminds
# them of the task and the hours left to complete it.

SENTINEL = "END"

def main():

    taskBox = []
    hourBox = []
    countOne = 0
    countTwo = 0
    typeTask = input("Please enter a task, or 'END' to stop:")

    while typeTask != SENTINEL:
        taskBox.append(typeTask)
        typeHour = int(input("Please enter the hour(s) needed to complete it"))
        hourBox.append(typeHour)
        typeTask = input("Please enter a task, or 'END' to stop:")
        countOne += 1
    print("Here is your task list:")
    while countTwo < countOne:
        print(hourBox[countTwo], "hours to complete :", taskBox[countTwo])
        countTwo += 1
main()
    
