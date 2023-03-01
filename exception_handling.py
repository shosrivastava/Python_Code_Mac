print("This code showcasses the Exception Handling in Python.\n")

def addFunc(num1,num2):
    try:
        return (num1 + num2)
    except Exception as e:
        return(e)

print(addFunc(10, 5))
print(addFunc(45, 'a'))
print(addFunc(50,50))