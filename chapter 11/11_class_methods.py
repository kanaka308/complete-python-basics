class Employee:
    company = "Camel"
    salary = 1000000
    location = "new york"

    def changeSallary(self, sal):
        self.__class__.salary = sal

    @classmethod

    def changeLocation(cls, loc):
        cls.location = loc


e = Employee()

print(e.salary)

e.changeSallary(45500000)

print(e.salary)

print(Employee.salary)

print("**********************************************")

print(Employee.location)

e.changeLocation('Delhi')

print(e.location)

print(Employee.location)

