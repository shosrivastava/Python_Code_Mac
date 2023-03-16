def myFunc(name, age, likes):
    sentence = "Hello {}. Your age is {} and you like {}.".format(name, age, likes)
    return sentence

myDict = {"age":28, "likes":"Python", "name":"XYZ"}

print(myFunc(**myDict))

# -----------------------------------------------------------

def foo(**kwargs):
    for key,value in kwargs.items():
        print("{}:{}".format(key, value))

foo(XYZ = "Male", DEF = "Female")