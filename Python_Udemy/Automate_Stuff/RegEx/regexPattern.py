myData = '''17-Apr-2021, 16-Apr-2021 and 18-Apr-2021.
The next dates are 26-04-2021, 06.05.2021 and 16/Jun/2021.

The mail IDs are aba2020@xyz.com, ask_help@demo.net and conc@demo.co.in.

The Phone numbers are +6032-007 1212, +6099.100 3344 and 017-9999880.'''

import re

myPattern1 = re.compile(r'\d{2}[-./]([a-zA-Z]{3}|\d{2})[-./]\d{4}')

match = myPattern1.finditer(myData)

print("The dates matched are:\n")

for i in match:
    print(i.group())

# For email:

print("\n")

myPattern2 = re.compile(r'\w+@[a-zA-Z]+(\.[a-z]{2,3})+')

print("The Email-IDs captured are:\n")

match = myPattern2.finditer(myData)

for i in match:
    print(i.group())

print("\n")

# For telephone number:

myPattern3 = re.compile(r'(\+\d)?\d{3}[-.]\d{3}\s?\d{4}')

match3 = myPattern3.finditer(myData)
print("The telephone numbers matched are:\n")

for i in match3:
    print(i.group())

print("\n")