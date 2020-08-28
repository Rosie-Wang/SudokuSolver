### SUDOKU for 9x9 Board ###
boardGiven = [
    [0,0,0,2,6,0,7,0,1],
    [6,8,0,0,7,0,0,9,0],
    [1,9,0,0,0,4,5,0,0],
    [8,2,0,1,0,0,0,4,0],
    [0,0,4,6,0,2,9,0,0],
    [0,5,0,0,0,3,0,2,8],
    [0,0,9,3,0,0,0,7,4],
    [0,4,0,0,5,0,0,3,6],
    [7,0,3,0,1,8,0,0,0]
]
boardGiven2 = [
    [0,0,0,6,0,0,4,0,0],
    [7,0,0,0,0,3,6,0,0],
    [0,0,0,0,9,1,0,8,0],
    [0,0,0,0,0,0,0,0,0],
    [0,5,0,1,8,0,0,0,3],
    [0,0,0,3,0,6,0,4,5],
    [0,4,0,2,0,0,0,6,0],
    [9,0,3,0,0,0,0,0,0],
    [0,2,0,0,0,0,1,0,0]
]

def printBoard(board):
    #BOARD STRUCTURING
    for i in range(0,9):
        if (i % 3 == 0) and (i != 0): #horizontally split the board every 3 lines (2 lines produced)
            print("------+------+------")
        for j in range(0,9):
            if (j % 3 == 0) and (j != 0): #vertically split the board every 3 lines (2 lines produced)
                print("|", end="")

    #NUMBERS IN BOARD
            if (j == 8): #when last element in each row is reached
                print(board[i][j]) #start a new line
            else:
                print(board[i][j],"", end="") #space out each number

def findEmpty(board):
    for i in range(0,9): #go through each row
        for j in range(0,9): #go through each column
            if board[i][j] == 0:
                return (i, j) #returns first empty spot come across
    return None #if there are no more empty spots

def isValid(board, num, posCoord): #want to insert num in posCoord = (row, col)
    posRow = posCoord[0]
    posCol = posCoord[1]
    #INVALID 1: Number exists in the row already, but not because we just inserted it
    for i in range(0,9):
        if board[posRow][i] == num and posCol != i:
            return False

    #INVALID 2: Number exists in the col already, but not because we just inserted it
    for i in range(0,9):
        if (board[i][posCol] == num) and (posRow) != i:
            return False

    #INVALID 3: Number exists in its mini square
    # Find the mini square we're inserting in
    squareX = posCol // 3 #column = 0/1/2
    squareY = posRow // 3 #row = 0/1/2
    actualSX = squareX * 3 #mini box start coordinates
    actualSY = squareY * 3 #mini square end coordinates

    # Check for repeats in the mini square we're inserting in
    for i in range(actualSY, actualSY + 3):
        for j in range(actualSX, actualSX + 3):
            if (board[i][j] == num) and ((i,j) != posCoord):
                return False

    #Passes all INVALID possibilies --> Yes, move is VALID!!!
    return True

def solveBoard(board): #recursion with base case = solved (board is full)
    found = findEmpty(board)
    #SOLVED
    if found is None: #board is full
        return True #therefore, board has been completely solved

    #UNSOLVED
    else:
        (foundRow,foundCol) = found #get coordinates of first empty space found
    for tryNum in range(1,10):
        if isValid(board, tryNum, (foundRow, foundCol)):
            board[foundRow][foundCol] = tryNum #insert the number if it's valid
            if solveBoard(board) == True: #check if board is solved
                return True
            else: #remove previously inserted number, and try another number
                board[foundRow][foundCol] = 0
    return False

print("Original: Easy")
printBoard(boardGiven)
solveBoard(boardGiven)
print("----------------------------------------")
print("Solved")
printBoard(boardGiven)

print("\nOriginal: Hard")
printBoard(boardGiven2)
solveBoard(boardGiven2)
print("----------------------------------------")
print("Solved")
printBoard(boardGiven2)