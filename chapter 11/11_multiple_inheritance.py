class employee:
    company = 'visa'
    eCode = 120

class freeliancer:
    company = 'fiver'
    level = 0

    def upgrade(self):
        self.level += 1

class programmer(employee, freeliancer):
    name = 'Shiva'


p = programmer()
print(p.eCode)
print(p.level)
print(p.company) #1st parent is given preference so company is "visa"


p.upgrade()

print(p.level)