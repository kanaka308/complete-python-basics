


class Number:
    def __init__(self, num1):
        self.num1 = num1

    def __add__(self, num2):
        print("Lets add")
        return self.num1 + num2.num1

    def __mul__(self, num2):
        print("Lets multiply")
        return self.num1 * num2.num1

    def __sub__(self, num2):
        print("Lets substract")
        return self.num1 - num2.num1
    
    
    def __floordiv__(self, num2):
        print('lets divide floor')
        return self.num1 / num2.num1

    def __truediv__(self, num2):
        print('lets divide true')
        return self.num1 / num2.num1

    

    
    
    


n1 = Number(10)
n2 = Number(20)

print(n1 + n2)
 
print(n1 * n2)

print(n2 - n1)

print(n2 // n1)

print(n2/n1)


