class Employee:
    company = "Google"
    salary = '100K'#class attribute

harry = Employee()
shiva = Employee()
print(shiva.salary)
print(harry.salary)

harry.salary = '900K'#instance attribute
shiva.salary = '1000K'#instance attribute

print(shiva.salary)
print(harry.salary)

print(shiva.company)
print(harry.company)


Employee.company = 'YouTube'
print(shiva.company) # changinges the values
print(harry.company)


shiva.age = 22 #instance attribute this is not present in above class

print(shiva.age)

print(shiva.adress) #rhrows an error as no attribute is present in instance and in class





