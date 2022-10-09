num = int(input('Enter your number: '))

table = [num * i for i in range(1,11)]

print(str(table))

with open('chapter 12/practise-12/table.txt', 'a') as f:
    f.write(str(table))
    f.write('\n')
    
