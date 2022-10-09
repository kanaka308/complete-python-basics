class Person:
    country = "India"

    def __init__(self):
        print("Initializing Person....\n")

    def takeBreath(self):
       
        print("Iam Breathing")

class Employee(Person):


    def __init__(self):
        super().__init__()
        print("Initializing Employee....\n")

    def getSallary(self):
        print(f'Sallary is{self.salary}')

    def takeBreath(self):
        super().takeBreath()

        print("Iam an employee so I am luckily breathing....")


class programmer(Employee):
    company = "Fiver"
    def __init__(self):
        super().__init__()
        print("Initializing programmer....\n")

    def getSallary(self):
        print('you don\'t get any sallary')

    def takeBreath(self):
        super().takeBreath()
        print("Iam a programmer so I am breathing++++...")


class python_programmer(programmer):
    def __init__(self):
        super().__init__()
        print("Initializing python_programmer....\n")

    def getSallary(self):
        print('you will get 1M sallary')

    def takeBreath(self):
        super().takeBreath()
        print("Iam a python_programmer I will breath fresh air...")





p = Person()

e = Employee()

pr = programmer()

py = python_programmer()


p.takeBreath()

print('******************************************************')

e.takeBreath()

print("******************************************************")

pr.takeBreath()

print("******************************************************")

py.takeBreath()






        

    




