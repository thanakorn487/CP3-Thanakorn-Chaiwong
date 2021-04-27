class Vehicle:
    LicenseCode = ""
    SerialCode = ""
    def AcOn(self):
        print("Turn On AC.")

class Car(Vehicle):
    def SayHello(self):
        print("Hello World!")

class PickUp(Vehicle):
    def SayGoodBye(self):
        print("Good Bye!")

class Van(Vehicle):
    def SayHi(self):
        print("Hi!")

Car_1 = Car()
Car_1.AcOn()
Car_1.SayHello()

Car_2 = PickUp()
Car_2.AcOn()
Car_2.SayGoodBye()

Car_3 = Van()
Car_3.AcOn()
Car_3.SayHi()