# game of life
# each cell with one or no neighbors dies, as if by solitude
# each cell with four or more neighbors dies, as if by overpopulation
# each cell with two or three neighbors survives
# each cell with three neighbors becomes populated

import os, sys
from time import sleep
from termcolor import colored

d = colored("-", "red")
O = colored("O", "green")

board = [
    [d, O, d, d, d, d, d, d],
    [d, d, O, d, d, d, O, d],
    [O, O, O, d, d, d, O, d],
    [d, d, d, d, d, d, O, d],
    [d, d, d, d, d, d, d, d],
    [d, d, d, d, d, d, d, d],
    [d, d, d, d, d, d, d, O],
    [d, d, d, d, d, d, d, d]
]

originalBoard = board

def generateBoard(board):
    for row in range(len(board)):
        current = ""
        #print(board[row])
        for column in range(len(board[row])):
            current += "| " + board[row][column] + " "
        print("---------------------------------")
        print(current + "|")
    print("---------------------------------")


def newGeneration():
    global board

    newBoard = [
    [d, d, d, d, d, d, d, d],
    [d, d, d, d, d, d, d, d],
    [d, d, d, d, d, d, d, d],
    [d, d, d, d, d, d, d, d],
    [d, d, d, d, d, d, d, d],
    [d, d, d, d, d, d, d, d],
    [d, d, d, d, d, d, d, d],
    [d, d, d, d, d, d, d, d]
    ]

    for row in range(len(board)):
        for column in range(len(board[row])):
            neighbors = 0
            if row == 0:
                if column == 0:
                    if board[row][column + 1] == O:
                        neighbors += 1
                    if board[row + 1][column] == O:
                        neighbors += 1
                    if board[row + 1][column + 1] == O:
                        neighbors += 1   
                if column > 0 and column < len(board[row]) - 1:
                    if board[row][column + 1] == O:
                        neighbors += 1
                    if board[row + 1][column] == O:
                        neighbors += 1
                    if board[row + 1][column + 1] == O:
                        neighbors += 1 
                    if board[row + 1][column - 1] == O:
                        neighbors += 1
                    if board[row][column - 1] == O:
                        neighbors += 1
                if column == len(board[row]) - 1:
                    if board[row][column - 1] == O:
                        neighbors += 1
                    if board[row + 1][column - 1] == O:
                        neighbors += 1
                    if board[row + 1][column] == O:
                        neighbors += 1
            if row > 0 and row < len(board) - 1:
                if column == 0:
                    if board[row][column + 1] == O:
                        neighbors += 1
                    if board[row + 1][column] == O:
                        neighbors += 1
                    if board[row + 1][column + 1] == O:
                        neighbors += 1 
                    if board[row - 1][column] == O:
                        neighbors += 1
                    if board[row - 1][column + 1] == O:
                        neighbors += 1
                if column > 0 and column < len(board[row]) -1:
                    if board[row - 1][column - 1] == O:
                        neighbors += 1
                    if board[row - 1][column] == O:
                        neighbors += 1
                    if board[row - 1][column + 1] == O:
                        neighbors += 1
                    if board[row][column + 1] == O:
                        neighbors += 1
                    if board[row + 1][column + 1] == O:
                        neighbors += 1
                    if board[row + 1][column] == O:
                        neighbors += 1
                    if board[row + 1][column - 1] == O:
                        neighbors += 1
                    if board[row][column - 1] == O:
                        neighbors += 1
                if column == len(board[row]) - 1:
                    if board[row][column - 1] == O:
                        neighbors += 1
                    if board[row + 1][column - 1] == O:
                        neighbors += 1
                    if board[row + 1][column] == O:
                        neighbors += 1
                    if board[row - 1][column] == O:
                        neighbors += 1
                    if board[row - 1][column - 1] == O:
                        neighbors += 1
            if row == len(board) - 1:
                if column == 0:
                    if board[row - 1][column] == O:
                        neighbors += 1
                    if board[row - 1][column + 1] == O:
                        neighbors += 1
                    if board[row][column + 1] == O:
                        neighbors += 1
                if column > 0 and column < len(board[row]) - 1:
                    if board[row - 1][column] == O:
                        neighbors += 1
                    if board[row - 1][column - 1] == O:
                        neighbors += 1
                    if board[row - 1][column + 1] == O:
                        neighbors += 1
                    if board[row][column - 1] == O:
                        neighbors += 1
                    if board[row][column + 1] == O:
                        neighbors += 1
                if column == len(board[row]) - 1:
                    if board[row - 1][column] == O:
                        neighbors += 1
                    if board[row - 1][column - 1] == O:
                        neighbors += 1
                    if board[row][column - 1] == O:
                        neighbors += 1
            
            if neighbors > 3:
                newBoard[row][column] = d
            elif neighbors == 3:
                newBoard[row][column] = O
            elif neighbors == 2:
                newBoard[row][column] = board[row][column]

    board = newBoard


generateBoard(board)

while True:
    print("""Instructions:
            y/n to continue
            5 or 10 for multiple generations
            reset to change to original board
    """)
    answer = input("--> ")
    if answer == "y":
        os.system("clear")
        newGeneration()
        generateBoard(board)

    elif answer == "n":
        break
    
    elif answer == "5":
        for i in range(5):
            os.system("clear")
            newGeneration()
            generateBoard(board)
            sleep(0.5)
    
    elif answer == "10":
        for i in range(10):
            os.system("clear")
            newGeneration()
            generateBoard(board)
            sleep(0.5)

    elif answer == "reset":
        os.system("clear")
        board = originalBoard
        generateBoard(board)

    else:
        print("You must answer with a y or n. ")