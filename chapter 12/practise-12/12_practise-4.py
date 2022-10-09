a = int(input('Enter 1st number: '))
b = int(input('Enter 2nd number: '))

try:
    print(a/b)

except ZeroDivisionError:
    print("Infinity")

finally:
    print("Code over")