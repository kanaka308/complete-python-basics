class Animals:
    animalType = "mammals"



class Pets(Animals):
    petType = "Cute"

class Cat(Pets):
    def meow(self):
        print("meow meow...!")

class Dog(Pets):
    @staticmethod
    def bark():
        print("bow bow...!")


c = Cat()

d = Dog()

print(c.animalType)
print(d.animalType)
print("*************************************")
print(c.petType)
print(d.petType)
print("**************************************")
c.meow()
d.bark()

