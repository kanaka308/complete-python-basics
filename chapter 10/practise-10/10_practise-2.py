


class Calculator:
    def __init__(self, num):
        self.number = num
    def square(self):
        print(self.number**2)

    def squareRoot(self):
        print(self.number**0.5)

    
    def cube(self):
        print(self.number**3)

    def cubeRoot(self):
        print(self.number**(1/3))

    @staticmethod
    def greet():
        print("**********************************Welcome Everyone******************************")


a = Calculator(5)
a.greet()
Calculator.square(a)
a.square()


a = Calculator(5)
Calculator.cube(a)
a.cube()

a = Calculator(25)
Calculator.squareRoot(a)
a.squareRoot()


a = Calculator(1000)
Calculator.cubeRoot(a)
a.cubeRoot()



b = Calculator(8000)
b.square()
b.squareRoot()
b.cube()
b.cubeRoot()













