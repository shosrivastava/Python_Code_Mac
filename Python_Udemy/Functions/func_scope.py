a = 250

def f1():
    a = 20
    print(a)

def f2():
    print(a + 100)

def f3():
    global a
    a = 500
    print(a)

f1()
f2()
f3()
print(a)