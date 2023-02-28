print("This code generates a random password with uppercase, lowecase characters along with numbers.\n")

from random import randint

password = ""

for i in range(5):
    i = chr(randint(65, 90))
    j = chr(randint(65, 90)).lower()
    k = randint(0, 10)
    password = str(password) + i + j + str(k)
print(f"The random generated password containing Uppercase, lowercase and numbers is {password}")
print(f"The length of the password is {len(password)}")
