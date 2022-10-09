class Person:
    country = "India"

    def __init__(self):
        print("initializing Person....\n")
    
    def giveCountry(self):
        print(self.country)
    
class Employee(Person):#inherits from person
    company = "Google"
    
    def __init__(self):
        print("initializing employee....\n")
    
 
    def giveCompany(self):
        print(f'This employee works at {self.company}')

class Programmer(Employee):#inherits both Person and Person but Person is given priority
    language = "python"
    company = "fiver"

    
    def __init__(self):
        print("initializing programmer....\n")
    

    def giveAll(self):
        print(f'iam a {self.language} programmer working at {self.company} lives in {self.country}')

    
    def giveCompany(self):
        print(self.company)
        super().giveCompany()

p = Person()

pr= Programmer()

e = Employee()

pr.giveAll()


# print(p.country)
# print(p.company)

# p.giveCountry()
# p.giveCompany()
# p.giveAll()
   

