class vehicle:
    licenseCode = ""
    serialCode = ""
    color = ""
    def turnonAirconditioner(self):
        print("Turn on: Air")

    def showColor(self):
        print(self.color)

class Car(vehicle):
    def sayHello(self):
        print("Say Hello World")

class Pickup(vehicle):
    pass

class Van(vehicle):
    pass

class Estatecar(vehicle):
    pass


Car1 = Car()
Car1.turnonAirconditioner()
Car1.sayHello()

Pickup1 = Pickup()
Pickup1.turnonAirconditioner()

Van1 = Van()
Van1.turnonAirconditioner()
Van1.color = "red"
Van1.showColor()

Estatecar1 = Estatecar()
Estatecar1.turnonAirconditioner()