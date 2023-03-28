print("This code shows the unpacking and packing concept for Arguments in Python.\n")

print("Unpacking of arguments.\n")

myString = "This is a string."
print("Below statement shows unpacking concept.\n")
print(*myString)

print("\n")

print("Packing of arguments.\n")

def add(*numbers):
    total = 0

    for i in numbers:
        total = total + i
    return total

myList = [1,2,3,4,5,6,7,8,9]
print(f"The sum of numbers from 1 to 9 is {add(*myList)}.\n")
