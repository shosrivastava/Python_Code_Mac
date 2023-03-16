def info(name, age, likes = "Python"):
    sentence = "Hey {}. You are {} years old and like {}.".format(name, age, likes)
    return sentence

print(info("Shobhit", 28))