# File:    decoder.py
# Started: by Dr. Gibson
# Author:  Nana Owusu
# Date:    10/18/17
# Section: 29
# E-mail:  onana1@umbc.edu
# Description:
#   This file contains python code that uses a function to 
#   pull out the uppercase letters from a list of strings
#   to decode a secret message.


######################################################################
# decode() decodes a message by extracting all of the 
#          capital letters to reveal the hidden meaning
# Input:   msgList; a list of strings
# Output:  secret;  a string containing the hidden message
def decode(msgList):
    secret = ""

    #-----------------------------------------------#
    # your code that goes through the list, finding #
    # the message hidden in the capitals, goes here #
    #-----------------------------------------------#
    secretBox = []
    index = 0
    count = 0
    while index < len(msgList):
        secretBox =  msgList[index]
        while count < len(secretBox):
            if secretBox[count].upper() == secretBox[count]:
                secret = secret + secretBox[count]
            count += 1
        count = 0
        index += 1
    return secret



def main():
    # message lists
    msg1 = ["thiS", "lifE", "Cannot", "Really", "bE", "True"]
    msg2 = ["wonDering", "hOw", "Good", "scoreS", "cAn", "regulaRly", \
                "bE", "manaGed", "yOu", "shOuld", "stuDy"]
    msg3 = ["studyinG", "Once", "thrOugh", "miDnight", "wiLl", \
                "caUse", "inComplete", "Knowledge", "Of", "iNformation", \
                "noT", "Helping", "thE", "earnEd", \
                "eXam", "grAde", "iMprove"]

    # calling the decode function for each
    ans1 = decode(msg1)
    ans2 = decode(msg2)
    ans3 = decode(msg3)

    # printing out the secret messages
    print("Message 1's secret was:")
    print(ans1)
    print()

    print("Message 2's secret was:")
    print(ans2)
    print()

    print("Message 3's secret was:")
    print(ans3)
    print()



main()

