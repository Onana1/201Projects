# File:    proj1.py
# Author:  Nana Owusu
# Date:    10/26/17
# Section: 29
# E-mail:  onana1@umbc.edu
# Description:
#   This program allows the user to select data from the CORGIS music library 
#   and loads that database selected, then the user is able to search the 
#   database or create a playlist that is based on a song's year, artist, or 
#   or genre.

# main menu options
USER_QUIT    = -1
MENU_SEARCH  = 0
MENU_CREATE  = 1

MAX_SONG_NUM = 10  # maximum number of songs in a playlist

# these constants are used to give names to the columns of the 2D list
YEAR     = 0
ARTIST   = 1
TITLE    = 2
GENRE    = 3
DURATION = 4
TEMPO    = 5

DETAIL_MIN = YEAR   # minimum value; used for getValidInput()
DETAIL_MAX = TEMPO  # maximum value

PLAYLIST_MIN = 1
PLAYLIST_MAX = 3

# THE REST OF YOUR CONSTANTS GO HERE!


############################################################################
# make2DList() constructs a 2D list from a file that contains information
#              about songs in a music library, such as year and artist
# Input:       filename;   a string of the music library's file name
# Output:      resultList; a 2D list of that file in the format below
#  __________________________________________________
# |   0  |    1   |   2   |   3   |     4    |   5   |
# |------|--------|-------|-------|----------|-------|
# | year | artist | title | genre | duration | tempo | 
# |--------------------------------------------------|
# | year | artist | title | genre | duration | tempo | 
# |--------------------------------------------------|
# | year | artist | title | genre | duration | tempo | 
# |--------------------------------------------------|
# | year | artist | title | genre | duration | tempo | 
#  --------------------------------------------------
def make2DList(filename):
    fileObj = open(filename)
    lines = fileObj.readlines()
    fileObj.close()

    resultList = []
    index = 0

    while index < len(lines):
        line = lines[index].strip().split(",")
        line[YEAR]     = int(line[YEAR]) 
        line[DURATION] = float(line[DURATION])
        line[TEMPO]    = float(line[TEMPO])
        resultList.append(line)
        index += 1

    return resultList

##################################################################
# getValidInput() gets a valid integer from the user that
#                 falls within the appropriate range; uses
#                 a prompt provided at function call
# Input:          prompt;  a string to use when asking for input
#                 minimum; a minimum integer
#                 maximum; a maximum integer
# Output:         userInput; an integer within the range

def getValidInput(prompt, minimum, maximum):
    numPrompt = int(input(prompt))
    while (numPrompt < minimum or  numPrompt > maximum) and numPrompt != -1:
        print("You enetered invalid input.")
        numPrompt = int(input(prompt))
            
    return numPrompt

##################################################################
# getValidInputNoQuit() gets a valid integer from the user that
#                 falls within the appropriate range without quit number
#                 ; uses a prompt provided at function call
# Input:          prompt;  a string to use when asking for input
#                 minimum; a minimum integer
#                 maximum; a maximum integer
# Output:         userInput; an integer within the range

def getValidInputNoQuit(prompt, minimum, maximum):
    numPrompt = int(input(prompt))
    while (numPrompt < minimum or  numPrompt > maximum):
        print("You enetered invalid input.")
        numPrompt = int(input(prompt))

    return numPrompt

        
##################################################################
# displayMainMenu() prints out the main menu of the program
# Input:            none
# Output:           none
def displayMainMenu():
    print("What would you like to do next?")
    print("     0) Perform a search")
    print("     1) Create a playlist")

##################################################################
# displayOptions() prints out a list of the six different
#                  attributes shown for each song
# Input:           none
# Output:          none
def displayOptions():
    print("     Index Value")
    print("     0 - Year")
    print("     1 - Artist")
    print("     2 - Title")
    print("     3 - Genre")
    print("     4 - Duration")
    print("     5 - Tempo")

##################################################################
# displayPLOptions() prints out the three different options
#                    for creating a playlist
# Input:             none
# Output:            none
def displayPLOptions():
    print("What playlist type do you want to create?")
    print("     1) Year Playlist")
    print("     2) Artist Playlist")
    print("     3) Genre Playlist")
    

##################################################################
# printSongs() prints the details of every song from a given
#              2D list
# Input:       songs;   Takes in a 2D list of songs
# Output:      none

def printSongs(songs):
    count = 0
    while count < len(songs):
        print(songs[count])
        count += 1
    
##################################################################
# colToString() converts a number to the corresponding column
#               heading
# Input:        column; an integer which is the index of the
#               column
# Output:       columnHeading; a string containing the column
#               heading

def colToString(column):
    columnWord = ""
    if column == YEAR:
        columnWord = "Year"
    if column == ARTIST:
        columnWord = "Artist"
    if column == TITLE:
        columnWord = "Title"
    if column == GENRE:
        columnWord = "Genre"
    if column == DURATION:
        columnWord = "Duration"
    if column == TEMPO:
        columnWord = "Tempo"
    return columnWord

##################################################################
# songToString() converts a song's information into a string
#               of it's details
# Input:        song;   1D list that contains the details of
#               a single song
# Output:       songString; a string containing the details
#               of the song

def songToString(song):
    songFinal = str(song[0]) +  " - " + song[3] + " - " + song[1] +  " - " + song[2]  
    return songFinal
        
##################################################################
# search() creates a 2D list of songs that match the value
#          being searched for in the selected column
# Input:   songs; a 2D list of songs
#          col;   an integer between 0-5
#          value; the value being searched for
# Output:  songSearched; a 2D list of all songs that match
#          the value in the selected column

def search(songs, col, value):
    row = 0
    songsFound = []
    while row < len(songs):
        colu = col
        if colu < len(songs[row]):
            if colu == 0 or colu == 4 or colu == 5:
                value = int(value)
            if colu == 0 or colu == 1 or colu == 2 or colu == 3:
                if songs[row][colu] == value:
                    songsFound.append(songs[row])
            if colu == 4 or colu == 5:
                if songs[row][colu] >= value:
                    songsFound.append(songs[row])
            row += 1
    return songsFound
            
##################################################################
# createPlaylist() creates a 2D list of all songs within the
#                  type selected by the user; limits list
#                  length using length in function call
# Input:           songs; a 2D list of songs
#                  choice; an integer between 1-3
#                  length; an integer between 0-10

def createPlaylist(songs, choice, length):
    if choice == 1:
        colu = YEAR
        value = "Year"
    if choice == 2:
        colu = ARTIST
        value = "Artist"
    if choice == 3:
        colu = GENRE
        value = "Genre"
    if choice == 2 or choice == 3:
        pickedValue = input("Enter a " + value + " to make a playlist of: ")
    if choice == 1:
        pickedValue = int(input("Enter a " + value + " to make a playlist of: "))
    row = 00
    plsongsFound = []
    while row < len(songs):
        if colu < len(songs[row]):
            if len(plsongsFound) < length:
                if songs[row][colu] == pickedValue:
                    plsongsFound.append(songs[row])
            row += 1
    if plsongsFound == []:
        print("Sorry, " + value + " " +  str(pickedValue) + " doesn't exist in your library.")
        print()
        print("Unable to create a playlist based on that criteria.")

    return plsongsFound
                
    


def main():
    print("This is the Music Organizer 3000!")
    print()

    songFile = input("Enter the filename of your song library: ")
    songList = make2DList(songFile)
    print()
    
    mainMenuPrompt = "Enter a menu choice (0-1) or '-1' to exit: "
    displayMainMenu()
    print()
    menuChoice = getValidInput(mainMenuPrompt, MENU_SEARCH, MENU_CREATE)
    
    while menuChoice != -1:
        if menuChoice == 0:
            columnPrompt = "Enter a column choice (0 - 5): "
            displayOptions()
            columnChoice = getValidInputNoQuit(columnPrompt, DETAIL_MIN, DETAIL_MAX)
            columnText = colToString(columnChoice)
            columnValue = input("Enter the value you want to search for " + columnText + " : ")
            newSongsFound = search(songList, columnChoice, columnValue)
            print()
            if newSongsFound == []:
                print("Your search returned no results.")
            else:
                print("Found the following:")
            counter = 0
            counter2 = 0
            songRow = []
            songTextList = []
            while counter < len(newSongsFound):
                songRow = newSongsFound[counter] 
                songInfo = songToString(songRow)
                songTextList.append(songInfo)
                counter += 1
            printSongs(songTextList)
            
            displayMainMenu()
            print()
            menuChoice = getValidInput(mainMenuPrompt, MENU_SEARCH, MENU_CREATE)

        if menuChoice == 1:
            playlistPrompt = "Choose a playlist to make?: "
            playlistLengthPrompt = "Enter the length of your playlist (0-10): "
            displayPLOptions()
            playlistChoice = getValidInput(playlistPrompt, PLAYLIST_MIN, PLAYLIST_MAX)       
            playlistLength = getValidInputNoQuit(playlistLengthPrompt, DETAIL_MIN, MAX_SONG_NUM) 
            newPlaylist = createPlaylist(songList, playlistChoice, playlistLength)
            print()
            if newPlaylist != []:
                print("Created this playlist:")
            counter = 0
            counter2 = 0
            songRow = []
            songTextList = []
            while counter < len(newPlaylist):
                songRow = newPlaylist[counter]
                songInfo = songToString(songRow)
                songTextList.append(songInfo)
                counter += 1
            printSongs(songTextList)
            print()
            


            displayMainMenu()
            print()
            menuChoice = getValidInput(mainMenuPrompt, MENU_SEARCH, MENU_CREATE)



    print("Thanks for using the Music Organizer 3000 come again!")
            
    
    

    
    

main()

