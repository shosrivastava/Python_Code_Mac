
def myFunc():
    num = (input("How many bikes do you own?\n"))

    try:
        if int(num) >= 2:
            print("Great, you've got many bikes!")
        else:
            print("You should keep checking for new launches.")

    except Exception as e:
        print(e)

myFunc()