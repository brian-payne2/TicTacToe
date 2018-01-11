import sys
import random

# Declare global variables
player1 = "X"
player2 = "O"


# Clear the board for a new game. Returns blank board
def newBoard():
    print("Let's play a new round of Tic Tac Toe!")
    new_board=[]
    for x in range(9):
        new_board.append(" ")
    return new_board

# Function to print the current status of the board
def printBoard(board):
    print("\n")
    for x in range(9):
        if x in [3, 6]:
            print("-----------")
        if x in [0, 1, 3, 4, 6, 7]:
            #line += " " + board[x] + " |"
            print(" " + board[x] + " |", end='')
        else:
            #line += " " + board[x]
            print(" " + board[x])
    print("\n")

# Take in player input. Returns the location in the list for inputted move
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

# Determine if the selected move is valid. Return True or False
def moveCheck(board, move):
    valid_move = False
    if board[move] == " ":
        valid_move = True
    return valid_move

# Function to determine if there is a winner. Returns True or False
def winner(board, mark):
    won = False
    if board[0] == mark:
        if board[1] == mark and board[2] == mark:
            won = True
        if board[3] == mark and board[6] == mark:
            won = True
        if board[4] == mark and board[8] == mark:
            won = True
    if board[1] == mark:
        if board[4] == mark and board[7] == mark:
            won == True
    if board[2] == mark:
        if board[4] == mark and board[6] == mark:
            won == True
        if board[5] == mark and board[8] == mark:
            won == True
    if board[3] == mark:
        if board[4] == mark and board[5] == mark:
            won == True
    if board[6] == mark:
        if board[7] == mark and board[8] == mark:
            won == True
    return won

# Function to determine who goes first
def firstMove():
    return random.randint(1,2)

# Function to determine if they want to play another game
def replay():
    answer = ""
    while answer not in ["yes", "no", "y", "n"]:
        answer = input("Do you want to play again? (yes/no): ")
        if answer.isalpha():
            answer = answer.lower()
            if answer in ["yes", "y"]:
                return True
            elif answer in ["no", "n"]:
                return False
            else:
                print("Please enter yes (y) or no (n) to proceed.")
        else:
            print("Please enter yes (y) or no (n) to proceed.")

# Driver Function
def driver():
    # Set up the game
    game_over = False
    first_move = firstMove()
    print("Player " + str(first_move) + " will go first")
    board = newBoard()
    printBoard(board)
    
    # Play the game
    while game_over == False:
        # Player 1 turn
        move_checked = False
        while move_checked == False:
            move = playerInput()
            if moveCheck(board, move):
                placeMarker(board, player1, move)
                printBoard(board)
                move_checked = True
            else:
                print("\n***\nThat space is already occupied, please choose an open space.\n***\n")
        
        # Post Player 1 turn
        if winner(board, player1):
            print("Congrats, " + str(player1) + " has won the game!")
            game_over = replay()
            break
        
        # Player 2 turn
        move_checked = False
        while move_checked == False:
            move = playerInput()
            if moveCheck(board, move):
                placeMarker(board, player2, move)
                printBoard(board)
                move_checked = True
            else:
                print("\n***\nThat space is already occupied, please choose an open space.\n***\n")
        
        # Post Player 2 turn
        if winner(board, player2):
            print("Congrats, " + str(player2) + " has won the game!")
            game_over = replay()
            break
    

    
    '''
    # Begin playing
    move1 = playerInput()
    placeMarker(board, player1, move1)
    printBoard(board)
    
    # test move check
    move2 = playerInput()
    if moveCheck(board, move2):
        placeMarker(board, player2, move2)
    
    # print board after move check
    printBoard(board)
    '''

#driver()
#replay()
