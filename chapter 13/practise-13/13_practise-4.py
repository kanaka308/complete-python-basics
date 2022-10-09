l = [1,2,5,10,15,15,12,13,45,55]

a = filter(lambda a: a%5==0, l)
print(list(a))