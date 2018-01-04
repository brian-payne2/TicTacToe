import sys

# Declare global variables
#board = []
player1 = "X"
player2 = "O"

# Function to print the current status of the board
def printBoard(board):
    for x in range(9):
        if x in [3, 6]:
            print("-----------")
        if x in [0, 1, 3, 4, 6, 7]:
            #line += " " + board[x] + " |"
            print(" " + board[x] + " |", end='')
        else:
            #line += " " + board[x]
            print(" " + board[x])

# Take in player input
def playerInput():
    int_move = 0
    while int_move not in range(1,10):
        move = input("Enter your move (1-9) where the top left box is 1 and bottom right is 9: ")
        try:
            int_move = int(move)
            if int_move not in range(1,10):
                print("Please enter a number between 1 and 9.")
        except ValueError:
            print("That's not an int!")
    return (int_move -1)

# Update board with player's mark
def placeMarker(board, player, move):
    board[move] = player

# Clear the board for a new game
def clearBoard():
    board=[]
    for x in range(9):
        board.append(" ")
    return board

# Driver Function
def driver():
    game_over = False
    board = clearBoard()
    printBoard(board)
    move1 = playerInput()
    placeMarker(board, player1, move1)
    printBoard(board)

#driver()
