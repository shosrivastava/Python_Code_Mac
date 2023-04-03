import random

print("Welcome, this is a Rock, Paper, Scissors game.\n")

print("The available options to play are: Rock, Paper and Scissors.\n")

options = ["rock", "paper", "scissors"]

while True:

    user_choice = input("Enter your choice:\n")

    user_choice = user_choice.lower()

    if user_choice not in options:
        print("You did not enter the correct choice. Please try again!\n")

        continue

    computer_choice = random.choice(options)

    print(f"You chose {user_choice} and computer chose {computer_choice}.\n")

    if user_choice == computer_choice:
        print("It's a tie!\n")

    elif user_choice == "rock" and computer_choice == "scissors":
        print("You win!\n")

    elif user_choice == "paper" and computer_choice == "rock":
        print("You win!\n")

    elif user_choice == "scissors" and computer_choice == "paper":
        print("You win!\n")

    else:
        print("Computer wins!\n")

    play_again = input("Do you want to continue? (yes or no)\n")

    play_again = play_again.lower()

    if play_again == "yes":
        continue
    else:
        break

print("Thanks for playing the game.\n")
