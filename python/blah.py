#tic-tac-Toe
from random import randint
from time import sleep
from termcolor import colored
import os
grid = ['', "1", "2", "3", "4", "5", "6", "7", "8", "9"]

X = colored("X", "green")

O = colored("O", "red")

filledspots = 0

def makegrid(grid):
  print(grid[1] + " | " + grid[2] + " | " + grid[3])
  print(grid[4] + " | " + grid[5] + " | " + grid[6])
  print(grid[7] + " | " + grid[8] + " | " + grid[9])
  
  
def checkspots(board):
    if board[1] == board[2] == board[3]:
        if board[1] == X:
            print(colored("You win!", "green"))
        else:
            print("You lose!")
        return True
    if board[4] == board[5] == board[6]:
        if board[4] == X:
            print("You win!")
        else:
            print("You lose!")
        return True
    if board[7] == board[8] == board[9]:
        if board[7] == X:
            print("You win!")
        else:
            print("You lose!")
        return True
    if board[1] == board[5] == board[9]:
        if board[1] == X:
            print("You win!")
        else:
            print("You lose!")
        return True
    if board[3] == board[5] == board[7]:
        if board[3] == X:
            print("You win!")
        else:
            print("You lose!")
        return True
    if board[3] == board[6] == board[9]:
        if board[3] == X:
            print("You win!")
        else:
            print("You lose!")
        return True
    if board[2] == board[5] == board[8]:
        if board[2] == X:
            print("You win!")
        else:
            print("You lose!")
        return True
    if board[1] == board[4] == board[7]:
        if board[1] == X:
            print("You win!")
        else:
            print("You lose!")
        return True
    



def game():
    grid = ['', "1", "2", "3", "4", "5", "6", "7", "8", "9"]
    filledspots = 0
    makegrid(grid)

    while True:
        player = int(input("Choose a spot:  "))
        while grid[player] == X or grid[player] == O:
            player = int(input("that's taken, where else?"))
        grid[player] = X

        os.system("clear")

        filledspots = filledspots + 1

        makegrid(grid)
        print("")
        if checkspots(grid) == True:
            break

        if filledspots == 9:
            print("T I E ! ! ! ")
            break

        cpu = randint(1, 9)

        while grid[cpu] == X or grid[cpu] == O:
            cpu = randint(1, 9)

        grid[cpu] = O

        filledspots = filledspots + 1

        sleep(1)
        makegrid(grid)
        if checkspots(grid) == True:
            break

    while True:
        answer = input("Do you want to play again? y/n: ")
        if answer == "n":
            print("see ya")
            break
        elif answer == "y":
            os.system("clear")
            game()
        else:
            print("You must choose y or n ")    

game()