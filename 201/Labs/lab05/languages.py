# File: languages.py
# Author: Nana Owusu
# Date: 10/5/2017
# Section: 29
# E-mail: onana1@umbc.edu
# Description: YOUR DESCRIPTION GOES HERE AND HERE
# YOUR DESCRIPTION CONTINUED SOME MORE

SENTINEL = 0

def main():

# types of programming languages to vote on
    languages = ["Python", "Java", "C++", "Ruby", "C", "PHP","Shakespeare"]
    count = 0
    votes = [0,0,0,0,0,0,0]
    while len(languages) > count:
        print(count + 1, "-", languages[count])
        count += 1
    numLang =  int(input("What language do you like? (Enter 0 to stop):"))
    while numLang != 0:
        votes[numLang - 1] += 1
        numLang = int(input("What language do you like? (Enter 0 to stop):"))
        print(votes)
    print("Python has", votes[0], "votes")
    print("Java has", votes[1], "votes")
    print("C++ has", votes[2], "votes")
    print("Ruby has", votes[3], "votes")
    print("C has", votes[4], "votes")
    print("PHP has", votes[5], "votes")
    print("Shakespeare", votes[6], "votes")
main()
