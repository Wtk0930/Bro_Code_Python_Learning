# prevents a user from creating an object of that class
# + compels a user to override abstract methods in a child class

# abstract class = a class which contains one or more abstract methods.
# abstract methods = a method has a declaration but does not have an implementation.

from abc import ABC, abstractmethod

# convert a normal class to a abstract class
class Vehicle(ABC):

    @abstractmethod
    def go(self):
        pass;


class Car(Vehicle):

    def go(self):
        print("You drive the Car");

class MotorCycle(Vehicle):

    def go(self):
        print("You ride the motorcycle");

vehicle = Vehicle();
car = Car();
motorcycle = MotorCycle();

vehicle.go();
car.go();
motorcycle.go();
