class Programmer:
    company = "Microsoft"
    def __init__(self, name, product):
        self.name = name
        self.product = product
    def getInfo(self):
        print(f'the name is {self.name} and the product is {self.product}')

shiva = Programmer("Shiva", "Skype")
hary = Programmer("hary", "GitHub")

Programmer.getInfo(shiva)
Programmer.getInfo(hary)

# or

shiva.getInfo()
hary.getInfo()