


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

    def __str__(self):
        return f"Decimal Number: {self.num1}"

    def __len__(self):
        return 1


n = Number(9)

print(n)

    

    
    
    



