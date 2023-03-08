print("This code showcases raising Exception in Python.\n")

def addNum(num1, num2):
    try:
        if (isinstance(num1, int) or isinstance(num1, float)) and (isinstance(num2, int) or isinstance(num2, float)):
            return (num1 + num2)
        else:
            raise Exception ("Only Integer and Float values are allowed.")
    except Exception as e:
        return (e)

print(addNum(10, 20))
print(addNum(50, '3'))
print(addNum(90, 10))