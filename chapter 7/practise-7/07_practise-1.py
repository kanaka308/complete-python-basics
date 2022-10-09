num = int(input('Enter the number whose table you want\n'))

# for i in range(11):
#     # print(num,'X',i,'=',num*i)
#     print(f'{num}X{i}={num*i}') #this is a f string

#Using while loop
i = 1
while i <= 10:
    print(f'{num}X{i}={num*i}')
    i += 1
