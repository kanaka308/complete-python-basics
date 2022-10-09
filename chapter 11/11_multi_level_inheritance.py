class Person:
    country = "India"
    
    def giveCountry(self):
        print(self.country)
    
class Employee(Person):#inherits from person
    company = "Google"

    def giveCompany(self):
        print(self.company)

class Programmer(Employee):#inherits both Person and Person but Person is given priority
    language = "python"

    def giveAll(self):
        print(f'iam a {self.language} programmer working at {self.company} lives in {self.country}')
p = Programmer()

print(p.country)
print(p.company)

p.giveCountry()
p.giveCompany()
p.giveAll()
   
