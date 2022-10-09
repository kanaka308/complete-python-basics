a = [3,6,5,5,6, 8, 9, 12, 14]

b = [i for i in a if i%2==0]#list comprehension
print(b)

c = {i for i in a}#set comprehension
print(c)
 