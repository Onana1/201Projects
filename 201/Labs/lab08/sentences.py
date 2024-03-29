# File:        sentences.py
# Started:     by Maria Brown (& Dr. Gibson)
# Author:      Nana Owusu
# Date:        10/26/2017
# Section:     29
# E-mail:      onana1@umbc.edu
# Description: This file contains python code that prints out the contents
#              of a 2D list of strings, and find the longest string in
#              each "sentence" (or row).

#-------------------------------------------------------------------------
# printSentences() prints the words in the given passage
# Input:           passage, a 2D list holding the passage
# Output:          None
#--------------------------------------------------------------------------
def printSentences(passage):

    print("Sentences:")
    print("---------------")
    index = 0
    counter = 0
    #loop through each sentence of the passage
    while index < len(passage):

        #----------------------------------------#
        # write a while loop that prints out the #
        # sentence, with no brackets or commas   #
        #----------------------------------------#
        while counter < len(passage[index]):
            print(passage[index][counter], end =" ")
            counter += 1
        print()
        counter = 0
        index += 1
#------------------------------------------------------------------
# tallyPassage() Finds total length of sentences
# Input:         passage, 2D list of sentences
# Output:        totalLength, int of the length of the passage
#                (also prints out length of each sentence)
#-----------------------------------------------------------------
def tallyPassage(passage):
    totalLength = 0

    passageIndex = 0
    #loop through the entire passage
    while passageIndex < len(passage):

        # count characters for this individual sentence
        characters = 0
        wordIndex = 0


        #----------------------------------------------------#
        # write a while loop that goes through an individual #
        # sentence's words and tallies the characters up     #
        #----------------------------------------------------#
        while wordIndex < len(passage[passageIndex]):
            characters += len(passage[passageIndex][wordIndex])


            wordIndex += 1


        # print how many total characters this individual sentence has
        print("Sentence", passageIndex,"has",characters,"characters")
        
        # add to running total of all characters
        totalLength += characters
        characters = 0
        passageIndex += 1

    #return the total number of characters
    return totalLength



def main():
    sentences = [["Here","comes","a","good","dog"], 
                 ["True","Grit","is","a","great","dog"], 
                 ["True","Grit","is","our","UMBC","mascot"], 
                 ["True","Grit","deserves","a","tennis","ball"]]

    
    # print the given sentences
    printSentences(sentences)
    
    ######################################################
    # write the line of code to call the tallyPassage() #
    # function -- pay attention to the input and output  #
    ######################################################
    totalNum = tallyPassage(sentences)
    

    # uncomment this line once tallyPassage() has been called
    print("The sentences have a total of", totalNum, "characters")
    
main()
