# File: proj3.py
# Author: Nana Owusu
# Date: 12/8/17
# Section: 29
# E-mail: onana1@umbc.edu
# Description:
# This program is a maze solver that takes a file from the
# user and constructs a maze based off that information, then finds the
# solution path through the maze or decides that there is no solution.

# smallest index of a list
MINIMUM = 0

# constants that denote the walls of the maze
RIGHT = 0
BOTTOM = 1
LEFT = 2
TOP = 3

############################################################################
# readMaze() reads in a file and constructs a 3D list from the file which 
#            contains information about the the maze, such as the length 
#            of the rows and columns, finishline, and walls
# Input:     filename;   a string of the maze's file name
# Output:    resultList; a 3D list that serves as the maze

def readMaze(filename):
    
    # reads in the file from the user
    ifp = open(filename, "r")
    mazeBounds = ifp.readline()
    mazeBoundsList = []
    # change the starting points into a list
    mazeBoundsList = mazeBounds.split()
    # change the starting points into integers
    mazeRow = int(mazeBoundsList[0])
    mazeCol = int(mazeBoundsList[1])
    
    # takes in the data of the file and turns it into a list
    mazePreList = ifp.readlines()
    ifp.close()
    count = 1
    mazeList = []
    while count < len(mazePreList):
        mazeList.append(mazePreList[count].split())
        count += 1
    
    # changes the elements within the list into integers
    row = 0
    while row < len(mazeList):
        col = 0
        while col < len(mazeList[row]):
            mazeList[row][col]= int(mazeList[row][col])
            col += 1
        row += 1

    rows = 0
    cols = 0
    maze = []
    
    # structure the maze data into a 3D list
    while cols < mazeRow:
        numRow = []
        while len(numRow) < mazeCol: 
            numRow.append(mazeList[rows])
            rows += 1 
        maze.append(numRow)
        cols += 1
    return maze

############################################################################
# finishMaze() aquires the finish points of the maze from a file with the
#              maze information
# Input:       filename; a string of the maze's file name
# Output:      userFinish; row and column postion of the finish

def finishMaze(filename):
    
    # reads in the file from the user
    ifp = open(filename, "r")
    mazeBounds = ifp.readline()
    mazeFinish = ifp.readline()
    mazeFinishList = []
    # change the finish points into a list
    mazeFinishList = mazeFinish.split()
    # change the elements of the list into integers
    count = 0
    while count < len(mazeFinishList):
         mazeFinishList[count] = int(mazeFinishList[count])
         count += 1
    return mazeFinishList

    
############################################################################
# searchMaze() returns a solution plan, if one is found using recursion
#              from a 3D list maze, the user's starting point, and the
#              finish point of the maze
# Input:       maze; 3D list of maze construct
#              userStart; row and column starting point of the maze
#              userFinish; row and column finish point of the maze
# Output:      mazePath; 2D list of maze solution path

def searchMaze(maze, startrow, startcol, endrow, endcol, mazeSolve):
    
    # makes squares of the maze in order to use global contants
    square = maze[startrow][startcol]

    # BASE CASES
    if square[RIGHT] == 1 and square[BOTTOM] == 1 and square[LEFT] == 1 and square[TOP] == 1:
        return

    # when the current points being looked at are the finish points 
    # end the function
    if startrow == endrow and startcol == endcol:
        print("Solution found!")
        mazeSolve.append([endrow, endcol])
        return mazeSolve

    # RECURSIVE CASE
    else:

        print("path currently", mazeSolve)
        print("visiting", [startrow,startcol])
        
        # right wall is only wall open and have already been right
        if square[RIGHT] == 0 and square[BOTTOM] == 1 and square[LEFT] == 1 and square[TOP] == 1 and [startrow,startcol + 1] in mazeSolve:
            
            mazeSolve.append([startrow, startcol])
            startrow = startrow
            startcol = startcol + 1
            mazeSolve.remove([startrow,startcol])

            newPath = []
            for i in range(len(mazeSolve)):
                innerCopy = list(mazeSolve[i] )
                newPath.append(innerCopy)

            return searchMaze(maze, startrow, startcol, endrow, endcol, newPath)
        # right wall is only wall open
        if square[RIGHT] == 0 and square[BOTTOM] == 1 and square[LEFT] == 1 and square[TOP] == 1:
            print("moving right")
            mazeSolve.append([startrow,startcol])
            newPath = []
            for i in range(len(mazeSolve)):
                innerCopy = list(mazeSolve[i] )
                newPath.append(innerCopy)
            return searchMaze(maze, startrow, startcol + 1, endrow, endcol, newPath)
        
        # right and left wall open and have already been right and left
        if square[RIGHT] == 0 and square[BOTTOM] == 1 and square[LEFT] == 0 and square[TOP] == 1 and [startrow,startcol + 1] in mazeSolve and [startrow,startcol - 1] in mazeSolve:

            mazeSolve.append([startrow, startcol])
            if mazeSolve[len(mazeSolve) - 2] == [startrow,startcol - 1]:
                startrow = startrow
                startcol = startcol + 1
            elif mazeSolve[len(mazeSolve) - 2] == [startrow,startcol + 1]:
                startrow = startrow
                startcol = startcol - 1
            mazeSolve.remove([startrow,startcol])
            
            newPath = []
            for i in range(len(mazeSolve)):
                innerCopy = list(mazeSolve[i] )
                newPath.append(innerCopy)

            return searchMaze(maze, startrow, startcol, endrow, endcol, newPath)
        # right and left wall open 
        elif square[RIGHT] == 0 and square[BOTTOM] == 1 and square[LEFT] == 0 and square[TOP] == 1: 
            mazeSolve.append([startrow,startcol])
            newPath = [] 
            for i in range(len(mazeSolve)):
                innerCopy = list(mazeSolve[i] )
                newPath.append(innerCopy)
            if [startrow,startcol + 1] not in mazeSolve:
                print("moving right")
                return searchMaze(maze, startrow, startcol + 1, endrow, endcol, newPath)
            elif [startrow,startcol - 1] not in mazeSolve:
                print("moving left")
                return searchMaze(maze, startrow, startcol - 1, endrow, endcol, newPath)


        # bottom wall only wall open and already went down
        if square[RIGHT] == 1 and square[BOTTOM] == 0 and square[LEFT] == 1 and square[TOP] == 1 and [startrow + 1,startcol] in mazeSolve:
            
            mazeSolve.append([startrow, startcol])
            startrow = startrow + 1
            startcol = startcol 
            mazeSolve.remove([startrow,startcol])

            newPath = []
            for i in range(len(mazeSolve)):
                innerCopy = list(mazeSolve[i] )
                newPath.append(innerCopy)

            return searchMaze(maze, startrow, startcol, endrow, endcol, newPath)
        # bottom wall only wall open
        elif square[RIGHT] == 1 and square[BOTTOM] == 0 and square[LEFT] == 1 and square[TOP] == 1:
            print("moving down")
            mazeSolve.append([startrow,startcol])
            newPath = []
            for i in range(len(mazeSolve)):
                innerCopy = list(mazeSolve[i] )
                newPath.append(innerCopy)
            return searchMaze(maze, startrow + 1, startcol, endrow, endcol, newPath)
        
        # left wall only wall open and already went left
        if square[RIGHT] == 1 and square[BOTTOM] == 1 and square[LEFT] == 0 and square[TOP] == 1 and [startrow,startcol - 1] in mazeSolve:
            
            mazeSolve.append([startrow, startcol])
            startrow = startrow 
            startcol = startcol - 1
            mazeSolve.remove([startrow,startcol])

            newPath = []
            for i in range(len(mazeSolve)):
                innerCopy = list(mazeSolve[i] )
                newPath.append(innerCopy)

            return searchMaze(maze, startrow, startcol, endrow, endcol, newPath)
        # left wall only wall open
        elif square[RIGHT] == 1 and square[BOTTOM] == 1 and square[LEFT] == 0 and square[TOP] == 1:
            print("moving left")
            mazeSolve.append([startrow,startcol])
            newPath = []
            for i in range(len(mazeSolve)):
                innerCopy = list(mazeSolve[i] )
                newPath.append(innerCopy)
            return searchMaze(maze, startrow, startcol - 1, endrow, endcol, newPath)
        
        # top wall only wall open and already went up
        if square[RIGHT] == 1 and square[BOTTOM] == 1 and square[LEFT] == 1 and square[TOP] == 0 and [startrow - 1,startcol] in mazeSolve:
            
            mazeSolve.append([startrow, startcol])
            startrow = startrow - 1
            startcol = startcol 
            mazeSolve.remove([startrow,startcol])

            newPath = []
            for i in range(len(mazeSolve)):
                innerCopy = list(mazeSolve[i] )
                newPath.append(innerCopy)

            return searchMaze(maze, startrow, startcol, endrow, endcol, newPath)
        # top wall only wall open
        elif square[RIGHT] == 1 and square[BOTTOM] == 1 and square[LEFT] == 1 and square[TOP] == 0:
            print("moving up")
            mazeSolve.append([startrow,startcol])
            newPath = []
            for i in range(len(mazeSolve)):
                innerCopy = list(mazeSolve[i] )
                newPath.append(innerCopy)
            return searchMaze(maze, startrow - 1, startcol, endrow, endcol, newPath)
        
        # bottom, left, and right wall are open
        elif square[RIGHT] == 0 and square[BOTTOM] == 0 and square[LEFT] == 0 and square[TOP] == 1:
            mazeSolve.append([startrow,startcol])
            newPath = []
            for i in range(len(mazeSolve)):
                innerCopy = list(mazeSolve[i] )
                newPath.append(innerCopy)
            if [startrow,startcol + 1] not in mazeSolve:
                print("moving right")
                return searchMaze(maze, startrow, startcol + 1, endrow, endcol, newPath)
            elif [startrow,startcol - 1] not in mazeSolve:
                print("moving left")
                return searchMaze(maze, startrow, startcol - 1, endrow, endcol, newPath)
            elif [startrow + 1][startcol] not in mazeSolve:
                print("moveing down")
                return searchMaze(maze, startrow + 1, startcol, endrow, endcol, newPath)

        # top, left, and right wall are open
        elif square[RIGHT] == 0 and square[BOTTOM] == 1 and square[LEFT] == 0 and square[TOP] == 0:
            mazeSolve.append([startrow,startcol])
            newPath = []
            for i in range(len(mazeSolve)):
                innerCopy = list(mazeSolve[i] )
                newPath.append(innerCopy)
            if [startrow,startcol + 1] not in mazeSolve:
                print("moving right")
                return searchMaze(maze, startrow, startcol + 1, endrow, endcol, newPath)
            elif [startrow,startcol - 1] not in mazeSolve:
                print("moving left")
                return searchMaze(maze, startrow, startcol - 1, endrow, endcol, newPath)
            elif [startrow - 1][startcol] not in mazeSolve:
                print("moving up")
                return searchMaze(maze, startrow - 1, startcol, endrow, endcol, newPath)

        # top, bottom, left and right wall are open
        elif square[RIGHT] == 0 and square[BOTTOM] == 1 and square[LEFT] == 0 and square[TOP] == 0:
            mazeSolve.append([startrow,startcol])
            newPath = []
            for i in range(len(mazeSolve)):
                innerCopy = list(mazeSolve[i] )
                newPath.append(innerCopy)
            if [startrow,startcol + 1] not in mazeSolve:
                print("moving right")
                return searchMaze(maze, startrow, startcol + 1, endrow, endcol, newPath)
            elif [startrow,startcol - 1] not in mazeSolve:
                print("moving left")
                return searchMaze(maze, startrow, startcol - 1, endrow, endcol, newPath)
            elif [startrow - 1,startcol] not in mazeSolve:
                print("moving up")
                return searchMaze(maze, startrow - 1, startcol, endrow, endcol, newPath)
            elif [startrow + 1,startcol] not in mazeSolve:
                print("moving down")
                return searchMaze(maze, startrow + 1, startcol, endrow, endcol, newPath)
            
        # bottom and left wall are open and already went down and left
        if square[RIGHT] == 1 and square[BOTTOM] == 0 and square[LEFT] == 0 and square[TOP] == 1 and [startrow + 1,startcol] in mazeSolve and [startrow,startcol - 1] in mazeSolve:

            mazeSolve.append([startrow, startcol])
            startrow = startrow + 1
            startcol = startcol
            mazeSolve.remove([startrow,startcol])

            newPath = []
            for i in range(len(mazeSolve)):
                innerCopy = list(mazeSolve[i] )
                newPath.append(innerCopy)
                
            return searchMaze(maze, startrow, startcol, endrow, endcol, newPath)

        # bottom and top wall are open
        elif square[RIGHT] == 1 and square[BOTTOM] == 0 and square[LEFT] == 0 and square[TOP] == 1:
            mazeSolve.append([startrow,startcol])
            newPath = []
            for i in range(len(mazeSolve)):
                innerCopy = list(mazeSolve[i] )
                newPath.append(innerCopy)
            if [startrow + 1,startcol] not in mazeSolve:
                print("moving down")
                return searchMaze(maze, startrow + 1, startcol, endrow, endcol, newPath)
            elif [startrow,startcol - 1] not in mazeSolve:
                print("moving left")
                return searchMaze(maze, startrow, startcol - 1, endrow, endcol, newPath)

        # right and bottom wall are open
        elif square[RIGHT] == 0 and square[BOTTOM] == 0 and square[LEFT] == 1 and square[TOP] == 1:
            mazeSolve.append([startrow,startcol])
            newPath = []
            for i in range(len(mazeSolve)):
                innerCopy = list(mazeSolve[i] )
                newPath.append(innerCopy)
            if [startrow + 1,startcol] not in mazeSolve:
                print("moving down")
                return searchMaze(maze, startrow + 1, startcol, endrow, endcol, newPath)
            elif [startrow,startcol + 1] not in mazeSolve:
                print("moving right")
                return searchMaze(maze, startrow, startcol + 1, endrow, endcol, newPath)

        # top and right wall are open
        elif square[RIGHT] == 0 and square[BOTTOM] == 1 and square[LEFT] == 1 and square[TOP] == 0:
            mazeSolve.append([startrow,startcol])
            newPath = []
            for i in range(len(mazeSolve)):
                innerCopy = list(mazeSolve[i] )
                newPath.append(innerCopy)
            if [startrow - 1,startcol] not in mazeSolve:
                print("moving up")
                return searchMaze(maze, startrow - 1, startcol, endrow, endcol, newPath)
            elif [startrow,startcol + 1] not in mazeSolve:
                print("moving right")
                return searchMaze(maze, startrow, startcol + 1, endrow, endcol, newPath)
        
        # top and left wall are open and already went left and top
        if square[RIGHT] == 1 and square[BOTTOM] == 1 and square[LEFT] == 0 and square[TOP] == 0 and [startrow - 1,startcol] in mazeSolve and [startrow,startcol - 1] in mazeSolve:

            mazeSolve.append([startrow, startcol])
            startrow = startrow 
            startcol = startcol - 1
            mazeSolve.remove([startrow,startcol])

            newPath = []
            for i in range(len(mazeSolve)):
                innerCopy = list(mazeSolve[i] )
                newPath.append(innerCopy)

            return searchMaze(maze, startrow, startcol, endrow, endcol, newPath)
        # top and left wall are open
        elif square[RIGHT] == 1 and square[BOTTOM] == 1 and square[LEFT] == 0 and square[TOP] == 0:
            mazeSolve.append([startrow,startcol])
            newPath = []
            for i in range(len(mazeSolve)):
                innerCopy = list(mazeSolve[i] )
                newPath.append(innerCopy)
            if [startrow - 1,startcol] not in mazeSolve:
                print("moving up")
                return searchMaze(maze, startrow - 1, startcol, endrow, endcol, newPath)
            elif [startrow,startcol - 1] not in mazeSolve:
                print("moving left")
                return searchMaze(maze, startrow, startcol - 1, endrow, endcol, newPath)
        
            
############################################################################
# getValidInputRow() gets a valid integer from the user that falls in the
#                 range of the list row or column; uses a prompt provided
#                 in function call
# Input:          prompt; a string tot use when asking for input
#                 minimum; a minimum integer of row or column
#                 maximum; a maximum integer of row or column
# Output:         userInput; an integer within the range

def getValidInput(prompt, minimum, maximum):
    rowNum = int(input(prompt))
    while rowNum < minimum or rowNum > maximum:
        rowNum = int(input("Invalid, enter a number a between " + str(minimum) +" and " + str(maximum-1) + " (inclusive): "))
    return rowNum

def main():

    
    print("Welcome to the Maze Solver!")
    
    # gets the filename and reads and creates the maze structure
    mazeFile = input("Please enter the filename of the maze: ")
    mazeList = readMaze(mazeFile)
    
    
    rowMax = len(mazeList)
    rowPrompt = "Please enter the starting row: "
    # gets the starting row
    startRow = getValidInput(rowPrompt, MINIMUM, rowMax)

    colMax = len(mazeList[0])
    colPrompt = "Please enter the starting column: "
    # gets the starting column
    startCol = getValidInput(colPrompt, MINIMUM, colMax)
    
    # put the finish points into variables 
    mazeEnd = finishMaze(mazeFile)
    endRow = mazeEnd[0]
    endCol = mazeEnd[1]
    
    # initializes the maze solution path list 
    mazeSolution = []
    
    # searches the maze from the starting point
    mazeSolvePath = searchMaze(mazeList, startRow, startCol, endRow, endCol, mazeSolution)
    
    # cuts up the solution path to go from the starting point
    mazeSolvedPath = []
    index1 = 0
    if mazeSolvePath != None:
        while index1 < len(mazeSolvePath):
            if mazeSolvePath[index1] == [startRow,startCol]:
                cutOff = index1
            index1 += 1
        mazeSolvedPath = mazeSolvePath[cutOff:len(mazeSolvePath)]
    
    # checks if something of value was returned and outputs solutions
    if mazeSolvePath != None: 
        index = 0
        while index < len(mazeSolvedPath):
            print(mazeSolvedPath[index])
            index += 1
    else:
        print("No solution found!")

main()
