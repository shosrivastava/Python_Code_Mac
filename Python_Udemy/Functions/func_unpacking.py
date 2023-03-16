def info(name, age, likes):
    sentence = "Hey {}, it's nice to meet you. You are {} year's old and like {}.".format(name, age, likes)
    return sentence

myDict = {"name": "Matt", "age": 35, "likes":"Coding"}

print(info(**myDict))