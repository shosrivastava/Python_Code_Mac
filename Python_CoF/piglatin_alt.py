print("This code converts a word into a Piglatin form.\n")

def myFunc(word):
    for i in range(len(word)):
        if word[i].lower() in "aeiou":
            return word[i: ] + word[: i] + "ay"

word = input("Enter a word: ")
print(f"{word} ----> {myFunc(word)}")