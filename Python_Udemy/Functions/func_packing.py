
def myFunc(*numbers):
    total = 0

    for i in numbers:
        total = total + i

    return total

print(myFunc(1,2,3,4,5,6,7,8,9))