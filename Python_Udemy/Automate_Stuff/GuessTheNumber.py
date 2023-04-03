print("Welcome, this is a guess the number game.\n")

import random

name = input("Please enter you name to continue..\n")

print(f"Hello {name}. I will guess a number between 1 and 10 and you will have to guess the same.\n")
print("You would get 5 chances to guess the correct number. Let's begin.\n")

guessNum = random.randint(1, 10)

count = 0

for i in range(1,5):
    count = i
    userChoice = int(input("Enter the number:\n"))

    if userChoice > guessNum:
        print("You guessed a bigger number.\n")
    
    elif userChoice == guessNum:
        print("Great, you guessed the correct number.\n")
        break
    
    else:
        print("You guessed a small number.\n")

print(f"You guessed the correct number in {count} turns.")