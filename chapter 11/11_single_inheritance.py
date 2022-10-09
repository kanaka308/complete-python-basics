class person:
    country = "india"
    gender = "male"
    def getInfo(self):
        print(self.country)
        print(self.gender)
class employee(person):
    company = "Google"
    salary = "1000k"
    unit = "web developer"

    def getInformation(self):
        print(f'works at {self.company}')
        print(f'salary is {self.salary}')
        print(f'sub unit is {self.unit}')

# a = person()
# a.getInfo()
a  = employee()
a.getInfo()

a.getInformation()
