# File: proj2.py
# Author: Nana Owusu
# Date: 11/10/2017
# Section: 29
# E-mail: onana1@umbc.edu
# Description: This program is Conway's game of life which is a program where
# the user selects the number of rows and columns, then selects where the cell 
# should turn on and how many iterations of the game should run.

# character for qutting the game
GAME_QUIT = "q"

# characters used in list(GameBoard)
PIXEL_DEAD = "."
PIXEL_ALIVE = "A"

# minimum values for creating rows and columns
ROW_MIN = 1
COL_MIN = 1

# minimum values for turning on a cell 
ROW_CELL_MIN = 0
COL_CELL_MIN = 0 

# minimum value for creating iterations
ITER_MIN = 0

############################################################################
# getValidInput() gets a valid integer from the user that is above an
#                 appropriate minimum, uses a prompt provided at function
#                 call
# Input:          prompt; a string that is used to ask for input
#                 minimum; minimum integer
# Output:         userInput; an integer above the minimum

def getValidInput(prompt, minimum):
    numPrompt = int(input(prompt))
    while numPrompt < minimum:
        print("This is not a valid value; please enter a number ")
        print("greater than or equal to " + str(minimum) + ".")
        numPrompt = int(input(prompt))

    return numPrompt

############################################################################
# getValidInputBoard() gets a valid integer from the user that is above the
#                      first index of a 2D list, and below the maximum index
#                      of the list, uses a prompt provided at function call
# Input:               prompt; a string that is used to ask for input
#                      minimum; minimum integer
#                      maximum; maximum integer
# Output:              userInput; an integer in the appropriate range

def getValidInputBoard(prompt, minimum, maximum):
    numPrompt = input(prompt)
    if numPrompt == GAME_QUIT:
        return numPrompt
    else:
        numPrompt = int(numPrompt)
        while numPrompt < minimum or numPrompt > maximum:
            print("That is not a valid value; please enter a number between " + str(minimum) + " and " + str(maximum) + " inclusive...")
            numPrompt = int(input(prompt))
        return numPrompt

############################################################################
# getValidInputBoardCol()gets a valid integer from the user that is above the
#                      first index of a 2D list, and below the maximum index
#                      of the list, uses a prompt provided at function call
# Input:               prompt; a string that is used to ask for input
#                      minimum; minimum integer
#                      maximum; maximum integer
# Output:              userInput; an integer in the appropriate range

def getValidInputBoardCol(prompt, minimum, maximum):
    numPrompt = int(input(prompt))
    while numPrompt < minimum or numPrompt > maximum:
        print("That is not a valid value; please enter a number between " + str(minimum) + " and " + str(maximum) + " inclusive...")
        numPrompt = int(input(prompt))
    return numPrompt

############################################################################
# nextIteration() gets the current condition of the game board and returns
#                 the next iteration of it
# Input:          userBoard; 2D list of current dead and alive pixels
# Output:         newBoard;  2D list of new dead and alive pixels

def nextIteration(gameBoard):
    # variables are used to indicate that a change in an element is needed 
    numCellDead = 0
    numCellAlive = 0
    # make a deep copy of the game board
    newGameBoard = [i[:] for i in gameBoard]
    row = 0 
    # code to iterate over the 2D list
    while row < len(gameBoard):
        col = 0 
        while col < len(gameBoard[row]):
            # looks around a dead element based on the game of life conditions
            if gameBoard[row][col] == PIXEL_DEAD:
                # above each condition in order to stay in index of the 2D list
                if row + 1 < len(gameBoard): 
                    if gameBoard[row+1][col] == PIXEL_ALIVE:
                        numCellDead += 1
                if row - 1 >= 0:
                    if gameBoard[row-1][col] == PIXEL_ALIVE:
                        numCellDead += 1
                if col + 1 < len(gameBoard[row]):
                    if gameBoard[row][col+1] == PIXEL_ALIVE:
                        numCellDead += 1
                if col - 1 >= 0: 
                    if gameBoard[row][col-1] == PIXEL_ALIVE:
                        numCellDead += 1
                if col + 1 < len(gameBoard[row]) and row + 1 < len(gameBoard):
                    if gameBoard[row+1][col+1] == PIXEL_ALIVE:
                        numCellDead += 1
                if col + 1 < len(gameBoard[row]) and row - 1 >= 0:
                    if gameBoard[row-1][col+1] == PIXEL_ALIVE:
                        numCellDead += 1
                if col - 1 >= 0 and row - 1 >= 0:
                    if gameBoard[row-1][col-1] == PIXEL_ALIVE:
                        numCellDead += 1
                if col - 1 >= 0 and row + 1 < len(gameBoard):
                    if gameBoard[row+1][col-1] == PIXEL_ALIVE:
                        numCellDead += 1
                # changes elements of deep copy to alive pixels
                if numCellDead == 3:
                    newGameBoard[row][col] = PIXEL_ALIVE
            # looks around an alive element for conditions
            if gameBoard[row][col] == PIXEL_ALIVE:
                if row + 1 < len(gameBoard):
                    if gameBoard[row+1][col] == PIXEL_ALIVE:
                        numCellAlive += 1
                if row - 1 >= 0:        
                    if gameBoard[row-1][col] == PIXEL_ALIVE:
                        numCellAlive += 1
                if col + 1 < len(gameBoard[row]):
                    if gameBoard[row][col+1] == PIXEL_ALIVE:
                        numCellAlive += 1
                if col - 1 >= 0:
                    if gameBoard[row][col-1] == PIXEL_ALIVE:
                        numCellAlive += 1
                if col + 1 < len(gameBoard[row]) and row + 1 < len(gameBoard):
                    if gameBoard[row+1][col+1] == PIXEL_ALIVE:
                        numCellAlive += 1
                if col + 1 < len(gameBoard[row]) and row - 1 >= 0:
                    if gameBoard[row-1][col+1] == PIXEL_ALIVE:
                        numCellAlive += 1
                if col - 1 >= 0 and row - 1 >= 0:
                    if gameBoard[row-1][col-1] == PIXEL_ALIVE:
                        numCellAlive += 1
                if col - 1 >= 0 and row + 1 < len(gameBoard):
                    if gameBoard[row+1][col-1] == PIXEL_ALIVE:
                        numCellAlive += 1
                # changes elements of the deep copy to dead or alive pixels
                if numCellAlive < 2:
                    newGameBoard[row][col] = PIXEL_DEAD
                elif numCellAlive >= 2 and numCellAlive <= 3:
                    newGameBoard[row][col] = PIXEL_ALIVE
                elif numCellAlive > 3:
                    newGameBoard[row][col] = PIXEL_DEAD
            col += 1
            # resets the variables for the next loop
            numCellAlive = 0
            numCellDead = 0
        row += 1
    return newGameBoard

############################################################################
# printBoard()  prints out the contents of the board
# Input:        userBoard; 2D list of dead and alive pixels
# Output        none

def printBoard(gameBoard):
    row = 0
    while row < len(gameBoard):
        col = 0
        while col < len(gameBoard[row]):
            print(gameBoard[row][col], end = " ")
            col += 1
        print()
        row += 1

############################################################################
# pixelAliveOn() modifies a 2D list by changing dead pixels to alive using
#                user input of the specfic row and column area
# Input:         userBoard; 2D list of dead and alive pixels
#                userRow; index of row
#                userColumn; index of column
# Output:        startBoard; 2D list where element of row/column specifed
#                is modified

def pixelAliveOn(userRow, userColumn, startBoard):
    # changes an element of the dead board to alive
    startBoard[userRow][userColumn] = PIXEL_ALIVE
    return startBoard
    
############################################################################
# createBoard() creates a 2D list of dead pixels using specified amount of
#               rows and columns
# Input:        userRows; length of rows
#               userColumns; length of columns
# Output:       gameBoard; 2D list of all starting dead pixels with
#               appropriate amount of rows and columns

def createBoard(rowLength, columnLength):
    gameBoard = []
    while len(gameBoard) < rowLength:
        boardRow = []
        while len(boardRow) < columnLength:
            boardRow.append(PIXEL_DEAD)
        gameBoard.append(boardRow)
    return gameBoard

def main():
    
    rowChoicePrompt = "Please enter number of rows: "
    rowChoice = getValidInput(rowChoicePrompt, ROW_MIN)
    
    colChoicePrompt = "Please enter the number of columns: "
    colChoice = getValidInput(colChoicePrompt, COL_MIN)
    
    # creates the board of dead cells based on users row and column amount 
    lifeBoard = createBoard(rowChoice, colChoice)
    
    rowCellPrompt = "Please enter the row of a cell to turn on(or q to exit): "
    rowCell = getValidInputBoard(rowCellPrompt, ROW_CELL_MIN, rowChoice - 1) 
    
    # reprompts user for alive cells until the user enters the sentinal value
    while rowCell != GAME_QUIT:
        
        colCellPrompt = "Please enter a column for that cell: "
        colCell = getValidInputBoardCol(colCellPrompt, COL_CELL_MIN, colChoice - 1)
        # turns the user selcted areas on the board from dead cells into alive 
        lifeBoard = pixelAliveOn(rowCell, colCell, lifeBoard)
        rowCellPrompt = "Please enter the row of a cell to turn on(or q to exit): "
        rowCell = getValidInputBoard(rowCellPrompt, ROW_CELL_MIN, rowChoice)
    
    # getting users number of iterations 
    iterationPrompt = "How many iterations should I run? "
    numIteration = getValidInput(iterationPrompt, ITER_MIN)
    
    # printing the starting board
    print("Starting Board:")
    print()
    printBoard(lifeBoard)
    
    # area of code where the different iterations are being printed
    iterationCount = 0
    while iterationCount < numIteration:
        iterationCount += 1
        lifeBoard = nextIteration(lifeBoard)
        print("Iteration " + str(iterationCount) + ":")
        printBoard(lifeBoard)
main()
