# Tic Tac Toe
#
#    x | o  | o
#  --------------
#    o | x  | x
#  --------------
#    o | x  | o
# 
# by Ryan

# import statements for helping with CPU opponent
# and animations
from random import *

# array of positions on the board
board = [" ", "1", "2", "3", "4", "5", "6", "7", "8", "9"]

# array of possible game over scenarios
winCases = [[1, 2, 3], [4, 5, 6], [7, 8, 9], [1, 4, 7], [2, 5, 8], [3, 6, 9], [1, 5, 9], [3, 5, 7]]

filledSpots = 0

# function to generate the tic tac toe grid using string concatenation
# with the positions of the board array
def generateBoard(board):
    print(" " + board[7] + " | " + board[8] + " | " + board[9])
    print("-----------")
    print(" " + board[4] + " | " + board[5] + " | " + board[6])
    print("-----------")
    print(" " + board[1] + " | " + board[2] + " | " + board[3])

# helper function to iterate through the winCases array and determine if any three
# spots on the board are the same
def checkResults(board):
    global filledSpots
    filledSpots += 1

    for i in range(8):
        if (board[winCases[i][0]] == board[winCases[i][1]] == board[winCases[i][2]]):
            if board[winCases[i][0]] == "X":
                print("You win!")

            else:
                print("You lose!")
            return True

    if filledSpots == 10:
        print("DRAW!")
        return True

    return False

# main game loop, will run until a break statement is reached
while True:

    # create the board
    generateBoard(board)

    # call the checkresults function and iterate through the winCases arrays
    # if there is a game winning scenario, end the loop
    if (checkResults(board) == True):
        break    

    # force the user to choose a valid position
    while True:
        playerChoice = int(input("What's your choice?: "))

        if board[playerChoice] != "X" and board[playerChoice] != "O":
            # reassign the board array at the position the player chose to an X
            board[playerChoice] = "X"  
            break

        else:
            print("That spot is taken.")

    print("You chose " + str(playerChoice))
    generateBoard(board)

    # call the checkresults function and iterate through the winCases arrays
    # if there is a game winning scenario, end the loop
    if (checkResults(board) == True):
        break

    while True: 
        cpuChoice = randint(1,9)

        if (board[cpuChoice] != "X") and (board[cpuChoice] != "O"):
            # reassign the board array at the position the computer chose to an O
            board[cpuChoice] = "O"
            break

    print("Computer's choice was " + str(cpuChoice))