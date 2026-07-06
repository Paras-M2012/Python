class A:
    def getA(self,a):
        self.a=a
    def putA(self):
        print(" A : ",self.a)

class B(A):
    def getB(self,b):
        self.b=b
    def putB(self):
        print(" B : ",self.b)

b1=B()
b1.getA(10)
b1.getB(30)
b1.putA()
b1.putB()


#2. Multi Level

class Drive:  
    def drive(self):  
        print("Drive safe")  

class Vehical(Drive):  
    def onRoad(self):  
        print("Vehical")  

class Car(Vehical):  
    def car_drive(self):  
        print("Car")  

obj=Car()
obj.drive()
obj.car_drive()
obj.onRoad()


#3. Multiple Ineheritance


class Camera:
    def take_photo(self):
        print("Taking a photo...")

class Phone:
    def make_call(self):
        print("Calling someone...")

class SmartPhone(Camera, Phone):
    def browse_internet(self):
        print("Browsing the internet...")


mobile = SmartPhone()

mobile.take_photo()
mobile.make_call()
mobile.browse_internet()



#4. Hybrid Inheritance

class Device:
    def power_on(self):
        print("Device is powered on.")

class Camera(Device):
    def record_video(self):
        print("Recording video...")


class Alarm(Device):
    def ring_alarm(self):
        print("Alarm is ringing...")

class SmartSecuritySystem(Camera, Alarm):
    def monitor_home(self):
        print("Monitoring the home.")


system = SmartSecuritySystem()

system.power_on()
system.record_video()
system.ring_alarm()
system.monitor_home()


#5. Hierarchical Inheritance :

class Vehicle:
    def start(self):
        print("Vehicle Started")

class Car(Vehicle):
    def drive(self):
        print("Car Is Driving")

class Bike(Vehicle):
    def ride(self):
        print("Bike Is Riding")

class Truck(Vehicle):
    def load_goods(self):
        print("Truck Is Carrying Good")


car = Car()
bike = Bike()
truck = Truck()


car.start()
car.drive()

bike.start()
bike.ride()

truck.start()
truck.load_goods()
