#Filter Syntax: list(filter(function, list))

def greater_than_5(num):
    if num>5:
        return True

    else:
        return False

l = [1,2,3,4,5,6,7,8,9,11,12,14,15]

print(list(filter(greater_than_5, l)))

print('*****************************************************')

g = lambda num:num>10
l1 = [1,2,3,4,5,12,13,14,15,166,14,16,89,90]
print(list(filter(g, l1)))
