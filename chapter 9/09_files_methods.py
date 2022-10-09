f = open('chapter 9/.another.txt', 'a')
b = f.write('I am apending')

f.close()

g = open('chapter 9/.another.txt', 'r')

c = g.read()
print(c)
g.close()








