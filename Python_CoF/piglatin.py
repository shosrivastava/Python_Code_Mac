# Step 1:
# Getting an input from the user in the form of a sentence.

original = input("Enter a sentence: ").strip().lower()

# Step 2:
# Split the sentence into words.

words = original.split()

# Step 3:
# Loop through each words to convert to pig latin.

new_words = []

for word in words:
    if word[0] in "aeiou":
        new_word = word + "yay"
        new_words.append(new_word)
    else:
        vowel_pos = 0

        for letter in word:
            if letter not in "aeiou":
                vowel_pos = vowel_pos + 1
            else:
                break
        cons = word[:vowel_pos]
        the_rest = word[vowel_pos :]

        new_word = the_rest + cons + "ay"

        new_words.append(new_word)

# Step 4:
# Sticking the words together.

output = " ".join(new_words)

# Step 5:
# Printing the output.

print(output)