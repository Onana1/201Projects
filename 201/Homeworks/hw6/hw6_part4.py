# File: hw6_part4.py
# Author: Nana Owusu
# Date: 11/21/16
# Section: 29
# E-mail: onana1@umbc.edu
# Description: This program ask the user for a word and checks whether or not 
# the word is a palindrome.

#############################################################
# reverseStr() uses recursion to reverse a string
# Input:       string; a string, the word being reversed 
#              count; an integer, the number used to iterate 
#              over the string 
# Output:      reversedstr; the string in reverse
def reverseStr(string, count):
    if count > len(string):
        return ""
    else: 
        return string[len(string) - count] + reverseStr(string, count + 1)

def main():
    
    wordCheck = input("Please enter a word to check for palindrome-ness: ")
    count = 1
    paliStr = reverseStr(wordCheck, count)
    if paliStr.lower() == wordCheck.lower():
        print("The word " +  wordCheck + " IS a palimdrome.")
    else:
        print("Sorry, the word" + wordCheck + " is NOT a palindrome.")
        print("Backwards, it becomes " + paliStr)

main()
