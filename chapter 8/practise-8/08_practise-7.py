def table(n):
    for i in range(1,11):
        print(f'{n}X{i}={n*i}')

n = int(input('Enter the number\n'))
print(table(n))