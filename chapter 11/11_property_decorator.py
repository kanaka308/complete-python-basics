class Employee:
    company = 'Bharat Gas'
    salary = 10000
    salarybonous = 1000


    @property  
    def totalSalary(self):
        return self.salary + self.salarybonous

    @totalSalary.setter
    def totalSalary(self, value):
        self.salarybonous = value - self.salary


e = Employee()

print(e.totalSalary)

print('******************************************')

e.totalSalary = 14000

print(e.salary)

print(e.salarybonous)
