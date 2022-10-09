class Employee: #creates a Class
    company = "Google"
    def getSallary(self):
        print("Sallary is 1000k")
        print(f'Sallary in {self.company} is {self.salary}')

harry = Employee() #Creates an Object
harry.salary = 1000000

Employee.getSallary(harry) #throws an Error if seif is not given above


harry.getSallary() #above line and this are same

