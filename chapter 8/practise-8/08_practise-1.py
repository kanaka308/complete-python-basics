from re import A


def greatestOf3(a,b,c):
    if a > b and a>c:
        return (f'{a} is the greatest')
    elif b>a and b>c:
        return (f'{b} is the greatest')
    else:
        return  (f'{c} is the greatest')

x = 3
y = 5
z = 100
print(greatestOf3(x,y,z))