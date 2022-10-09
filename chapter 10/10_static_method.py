#to an object which takes no arguent
class Employee: #creates a Class
    company = "Google"
    def getSalary(self, signature):
        print("Sallary is 1000k")
        print(f'Sallary in {self.company} is {self.salary}\n{signature}')

#     def greet():#throws an error
#         print('Good morning sir')

# hary = Employee()
# hary.greet()

    @staticmethod #does not give error ow
    def greet():
        print('Good morning sir')

hary = Employee()
hary.salary = 100000
hary.getSalary("thanks")
hary.greet()
