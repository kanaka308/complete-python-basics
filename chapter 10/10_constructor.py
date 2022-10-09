class Employee:
    company = "Google"
    def __init__(self, name, salary, subunit):#this is executed whether you call it or not
        self.name = name
        self.salary = salary
        self.subunit = subunit
        print("Employee is created")
    

    def getDetails(self):
        print(f'name is {self.name}')
        print(f'Salary is {self.salary}')
        print(f'sub unit is {self.subunit}')



shiva = Employee("Shivanand", 100000, 'web-developer')

shiva.getDetails()