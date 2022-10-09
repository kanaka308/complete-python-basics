from re import A


with open('chapter 9/sample.txt', 'r') as f:
    a = f.read()
    print(a)

with open('chapter 9/sample.txt', 'w') as f:
    a = f.write('Hello')
print(a)



