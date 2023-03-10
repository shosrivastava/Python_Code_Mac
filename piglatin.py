print("This code is used to display a sentence in pig-latin form.\n")

entered_sentence = input("Enter a sentence:\n").strip().lower()

split_words = entered_sentence.split()

new_words = []

for i in split_words:
    if i[0] in "aeiou":
        new_word = i + "yay"
        new_words.append(new_word)

    else:
        vowel_pos = 0
        for j in i:
            if j not in "aeiou":
                vowel_pos = vowel_pos + 1
            else:
                break
        cons = i[ : vowel_pos]
        the_rest = i[: vowel_pos]
        new_word = the_rest + cons + "ay"

        new_words.append(new_word)

new_sentence = " ".join(new_words)

print(new_sentence)