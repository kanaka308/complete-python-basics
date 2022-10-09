a = 54 #Global Variable

def func1():
    a = 8 #Local variabla
    print(a)

func1()

print(a)
 
print('*********************************')

b = 99
def func2():
    global b
    b = 100
    print(b)

func2()
print(b)
