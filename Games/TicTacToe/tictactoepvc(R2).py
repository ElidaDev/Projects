import string
import random as rand

gameBoard = [
["1", "2", "3"],
["4", "5", "6"],
["7", "8", "9"]   
]

selection = {
    1:[0,0],
    2:[0,1],
    3:[0,2],
    4:[1,0],
    5:[1,1],
    6:[1,2],
    7:[2,0],
    8:[2,1],
    9:[2,2]
}

#print the board
def drawBoard(board):
    for r in range(3):
        print(f"{board[r][0]}|{board[r][1]}|{board[r][2]}")
        print(f"-"*5)
    pass

def checkDraw(board):
    for eachRow in board:
        if any(char in string.digits for char in eachRow):
            return False
    print("Tie")
    return True

def checkHorizontal(board):
        for r in range(len(board)):    
            if(board[r][0]==board[r][1] and board[r][0] == board[r][2]):
                symbol = board[r][0]
                print(f"Winner: {symbol}")
                return True
        return False

def checkVertical(board):
        for c in range(len(board)):    
            if(board[0][c]==board[1][c] and board[0][c] == board[2][c]):
                symbol = board[0][c]
                print(f"Winner: {symbol}")
                return True
        return False
                
def checkDiagonal(board):
    if (board[0][0] == board[1][1] and board[0][0] == board[2][2]):
        symbol = board[0][0]
        print(f"Winner: {symbol}")
        return True
    elif (board[0][2] == board[1][1] and board[0][2] == board[2][0]):
        symbol = board[0][2]
        print(f"Winner: {symbol}")
        return True
    return False
        
def checkWinner(board):
    drawBoard(board)
    if checkHorizontal(board) or checkVertical(board) or checkDiagonal(board) or checkDraw(board):
        return True
    return False

def swapTurn(turn):
    if turn:
        return 'X'
    else:
        return 'O'

def checkSpot(symbol,board,row,col):
    if board[row][col] != 'X' and board[row][col] != 'O':
        board[row][col] = symbol
        return False
    return True

def freeSpot(board,row,col):
    if board[row][col] != 'X' and board[row][col] != 'O':
        return True
    return False

def pickSpot(board):
    # Check for Horizontal wins
    for r in range(len(board)):
        if (board[r][0] == board[r][1] and board[r][0] == 'O' and freeSpot(board,r,2)):
            return r,2
        elif (board[r][1] == board[r][2] and board[r][1] == 'O' and freeSpot(board,r,0)):
            return r,0
        elif (board[r][0]==board[r][2]) and board[r][2] == 'O' and freeSpot(board,r,1):
            return r,1
    # Check for vertical wins
    for c in range(len(board)):
        if (board[0][c] == board[1][c] and board[0][c] == 'O' and freeSpot(board,2,c)):
            return 2,c
        elif (board[1][c] == board[2][c] and board[1][c] == 'O' and freeSpot(board,0,c)):
            return 0,c
        elif (board[0][c]==board[2][c] and board[0][c] == 'O' and freeSpot(board,1,c)):
            return 1,c
    #Check for Diagonal Wins
    #/
    if board[0][0] == board[1][1] and board[0][0] == 'O' and board[2][2] == '9':
        return 2,2
    elif board[1][1] == board[2][2] and board[1][1] == 'O' and board[0][0] == '1':
        return 0,0
    # \
    elif board[0][2] == board[1][1] and board[1][1] == 'O' and board[2][0] == '7':
        return 2,0
    elif board[1][1] == board[2][0] and board[2][0] == 'O' and board[0][2] =='3':
        return 0,2
    # Check if Horizontal needs defended
    for r in range(len(board)):
        if (board[r][0] == board[r][1] and freeSpot(board,r,2)):
            return r,2
        elif (board[r][1] == board[r][2] and freeSpot(board,r,0)):
            return r,0
        elif (board[r][0]==board[r][2]) and freeSpot(board,r,1):
            return r,1
    # Check if Vertical needs defended
    for c in range(len(board)):
        if (board[0][c] == board[1][c] and freeSpot(board,2,c)):
            return 2,c
        elif (board[1][c] == board[2][c] and freeSpot(board,0,c)):
            return 0,c
        elif (board[0][c]==board[2][c] and freeSpot(board,1,c)):
            return 1,c
    # Check if Topleft to bottom right needs defended
    if board[0][0] == board[1][1] and board[2][2] == '9':
        return 2,2
    elif board[0][0] == board[2][2] and board[1][1] == '5':
        return 1,1
    elif board[1][1] == board[2][2] and board[0][0] == '1':
        return 0,0
    # Check if Topright to bottom left needs defended
    elif board[0][2] == board[1][1] and board[2][0] == '7':
        return 2,0
    elif board[0][2] == board[2][0] and board[1][1] == '5':
        return 1,1
    elif board[1][1] == board[2][0] and board[0][2] =='3':
        return 0,2
    return 9,9

symbol = 'X'
turn = True
print("Welcome to TicTac Toe")

while(symbol != 'q'):
    if symbol == 'X':    
        print("")
        drawBoard(gameBoard)
        valid = False

        while not valid:
            print("")
            spot = int(input("Select a spot: "))-1
            print("")
            if spot in range(9):
                row = selection[spot+1][0]
                col = selection[spot+1][1]
                if checkSpot(symbol,gameBoard,row,col):
                    print("Spot Taken")
                else:
                    valid = True
                    
        if checkWinner(gameBoard): 
            symbol = 'q'
        else:
            symbol = 'O'
    else:
        valid = False
        while not valid:
            row,col = pickSpot(gameBoard)
            if row == 9: 
                spot = rand.randint(1,9)
                row = selection[spot][0]
                col = selection[spot][1]
            if checkSpot(symbol,gameBoard,row,col):
                print(f"Spot Taken at ({row},{col})")
            else:
                valid = True
        if checkWinner(gameBoard): 
            symbol = 'q'
        else:
            symbol = 'X'