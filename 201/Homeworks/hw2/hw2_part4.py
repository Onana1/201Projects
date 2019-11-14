# File: hw2_part4.py
# Author: Nana Owusu
# Date: 9/22/2017
# Section: 29
# E-mail: onana1@umbc.edu
# Description: This prorgam ask the user for two numbers and the operation that
# they want done on the operation and the problem is displayed.

def main():

    print("You can do many operation with this program:add, subtract, multiply, divide, int divide, mod, and exponents.")
    
    typeOperation = input("What operation do you want to perform?")
    numFirst = int(input("Enter the first number of the operation?:"))
    numSecond = int(input("Enter the second number of the operation?:"))

    operAdd = numFirst + numSecond
    operSub = numFirst - numSecond
    operMult = numFirst * numSecond
    operDiv = numFirst / numSecond
    operIntDiv = numFirst // numSecond
    operMod = numFirst % numSecond
    operExpo = numFirst ** numSecond

    if typeOperation == "add":
        print(numFirst, "+" ,numSecond, "=" ,operAdd)
    elif typeOperation  == "subtract":
        print(numFirst, "-" ,numSecond, "=" ,operSub)
    elif typeOperation == "multiply":
        print(numFirst, "x" ,numSecond, "=" ,operMult)
    elif typeOperation == "divide":
        print(numFirst, "/" ,numSecond, "=" ,operDiv)
    elif typeOperation == "int divide":
        print(numFirst, "//" ,numSecond, "=" ,operIntDiv)
    elif typeOperation == "mod":
        print(numFirst, "%" ,numSecond, "=" ,operMod)
    elif typeOperation == "exponents":
        print(numFirst, "^" ,numSecond, "=" ,operExpo)
    else:
        print("Invalid Operation")

main()

