# File: adoptions.py
# Author: Nana Owusu
# Date: 11/30/17
# Section: 29
# E-mail: onana1@umbc.edu
# Description:
# DESCRIPTION OF WHAT THE PROGRAM DOES

def main():

    print("Dogs are brought to adoption events based on time at the shelter")
    minStay = input("Please enter the minimum stay time for the dogs: ")

    ifp = open("dogData.txt")
    dataDogs = ifp.readlines()
    ifp.close()
    ifp2 = open("listDogs.txt", "w")
    ifp2.close()
    for i in range(len(dataDogs)):
        dataDawgs = dataDogs[i].split(",")
        name = dataDawgs[0]
        breed = dataDawgs[1]
        gender = dataDawgs[2]
        age = dataDawgs[3]
        length = dataDawgs[4]
        
        
        if (int(length) >= int(minStay)):
            ifp2.write(",".join(dataDawgs))
            
    print(dataDogs)

main()
