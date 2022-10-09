try:
    a = int(input('enter a number: '))
    b = 1
    print(b/a)

except ValueError as e:
    print(f"exception1 occured\n{e}")



except ZeroDivisionError as f:
    print(f'exception2 occured\n{f}')


print('Thanks for using this code')