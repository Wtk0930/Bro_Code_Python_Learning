class Animal:

    def eat(self):
        print("This animal is eating");


class Rabbit(Animal):

    # override the eat method more specifically
    def eat(self):
        print("This rabbit is eating a carrot");

rabbit = Rabbit();
rabbit.eat();
