
f = open('chapter 9\sample.txt', 'r')#use open function to open a file
f = open('chapter 9\sample.txt')#by default the mode is read
data = f.read()#use read function to read that file
print(data)



 
f.close() #must close every file after opening
f = open('chapter 9\sample.txt')

data1 = f.read(10) # prints first 10 letters
print(data1)
f.close()

g = open('chapter 9\sample.txt')

data2 = g.readline() # reads first line of the file
print(data2)
g.close()

