import datetime, random as rn
import sys
import webbrowser as wb
import countVowels

# print(f"Today's date is {datetime.date.today()}")

# print("Random number is", rn.randint(1,10))

# wb.open("https://www.google.com")

name = input("Enter a name:\n")

print("The number of vowels are", countVowels.countVow(name))

# print("\n")
# print(sys.path)