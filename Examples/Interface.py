from pysha import *


@interface
class Car:
    name = None
    speed = 0

    def setSpeed(self, speed):
        pass

    def getSpeed(self):
        pass


@interface(Car)
class Tesla:
    name = "Tesla"
    speed = 0

    def setSpeed(self, speed):
        self.speed = speed

    def getSpeed(self):
        return self.speed


@interface(Car)
class BMW:
    name = "BMW"
    speed = 0

    def setSpeed(self, speed):
        self.speed = speed

    def getSpeed(self):
        return self.speed


a = BMW()
