print("This code simulates a baby asking random questions.\n")

from random import choice

question_set = ["Why is the sky blue?", "What is a rainbow?", "Why is the moon white?"]

question_asked = choice(question_set)

print(question_asked)
print("\n")

answer = input("Your answer..\n").strip().capitalize()

while answer != "I don't know":
    answer = input("Why?\n").strip().capitalize()