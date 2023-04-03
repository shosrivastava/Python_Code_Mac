import pprint

print("This code will count the number of letters in a given string.\n")

myString = input("Enter a string to proceeed:\n")

letter_count = {}

for i in myString:
    # if i.isalpha():
        if i.lower() in letter_count:
            letter_count[i.lower()] += 1
        else:
            letter_count[i.lower()] = 1

pprint.pprint(letter_count)