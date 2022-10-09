#Greatest of 4 numbers
num1 = int(input('enter num1\n'))
num2 = int(input('enter num2\n'))
num3 = int(input('enter num3\n'))
num4 = int(input('enter num4\n'))

# allNum =[num1,num2,num3,num4]
# print('all numbers are:', allNum)

# if num1>num2 and num1>num3 and num1>num4:
#     print('num1 is greater')
# elif num2>num3 and num2>num4 and num2>num1:
#     print('num2 is greater')
# elif num3>num1 and num3>num2 and num3>num4:
#     print('num3 is greater')
# else:
#     print('num4 is greater')

if num1>num4:
    f1 = num1
else:
    f1 = num4

if num3>num2:
    f2 = num3
else:
    f2 = num2
if f1>f2:
    print(f1, "is greatest")
else:
    print(f2, "is greatest")

