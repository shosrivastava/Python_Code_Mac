print("This code shows the unpacking and packing concept of Keywords in Python.\n")

#  Unpacking of keyword arguments.

def intro(name, age, likes):
    statement = "Hey {}, you are {} years old and like {}.".format(name, age, likes)
    return statement

myDict = {"name": "XYZ", "age": 28, "likes": "Python"}

print(intro(**myDict))

# Packing of keyword arguments.

print("\n")
print("Below is the concept of packing of keyword arguments.\n")

def myFunc(**kwargs):
    for key, value in kwargs.items():
        print ("{}:{}".format(key, value))

(myFunc(name = "XYZ", Occupation = "Coder"))