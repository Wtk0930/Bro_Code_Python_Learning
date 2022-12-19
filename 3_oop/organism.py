class Organism:
    alive = True;

class Animal(Organism):

    def eat(self):
        print("The animal is eating!");

class Dog(Animal):

    def bark(self):
        print("This dog is barking!");
