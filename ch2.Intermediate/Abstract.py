from abc import ABC, abstractmethod

class Vehicle(ABC):

    @abstractmethod
    def go():
        pass
    @abstractmethod
    def stop():
        pass


class Car(Vehicle):

    def go(self):
        print("You drive the car!")

    def stop(self):
        print("You stop the car!")

car = Car()

car.go()
car.stop()