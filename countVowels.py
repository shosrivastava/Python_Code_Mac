print("This code counts the number of vowels in a given string.\n")

def countVow(myString):
    
    vow = ["a","e","i","o","u"]
    count = 0

    for i in myString:
        if i.lower() in vow:
            count += 1
    print(f"Total number of vowels in the string are {count}.")