print("This code is for the Rock, Paper and Scissors game.\n")

from random import randint

moves = ['rock', 'paper', 'scissors']

while True:
    computer = moves[randint(0,2)]
    player = input("Enter your choice from 'rock, 'paper or 'scissors' or 'q' to quit the game. ").lower()

    if player == 'q':
        print("You have chosen to end the game. Thanks for playing!")
        break
    elif player == computer:
        print("It's a tie as you and the cmputer selected the same options.")
    elif player == 'rock':
        if computer == 'paper':
            print("You loose as computer selected " + computer)
        else:
            print("You win as computer selected " + computer)
    elif player == 'paper':
        if computer == 'rock':
            print("You win as computer selected " + computer)
        else:
            print("You loose as computer selected " + computer)

    elif player == 'scissors':
        if computer == 'rock':
            print("You loose as computer selected " + computer)
        else:
            print("You win as computer selected " + computer)
    else:
        print("You did not enter the correct choice. Please try again!")