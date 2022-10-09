class Train:
    def __init__(self, name, fare, seats):
        self.name = name
        self.fare = fare
        self.seats = seats

    def getStatus(self):
        
        
        print(f'the name of train is {self.name}')
        print(f'the seats availabe are {self.seats}')

        
    def fareInfo(self):
        print(f'The price of ticket is {self.fare}')

    def bookTicket(self):
        if self.seats>0:
            print(f'your seat is booked, your seat number is {self.seats}')
            self.seats -= 1
        else:
            print('sorry train is full!')

    def cancelTicket(self):
        print(f'you ticket of {self.seats+1 } has been cancelled')
        self.seats += 1

golgumbaz_express = Train("golgumbaz_express123", 400, 1000)

golgumbaz_express.getStatus()
golgumbaz_express.fareInfo()

golgumbaz_express.bookTicket()
golgumbaz_express.bookTicket()
golgumbaz_express.bookTicket()
golgumbaz_express.bookTicket()
golgumbaz_express.bookTicket()
golgumbaz_express.cancelTicket()

golgumbaz_express.getStatus()
 
