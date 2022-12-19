from animal import Animal;

# inherit the Animal class
class Rabbit(Animal):
    # create unique methods
    def run(self):
        print("This rabbit is running");

class Fish(Animal):
    def swim(self):
        print("this fish is swimming");
        return self;

class Hawk(Animal):
    def fly(self):
        print("this hawk is flying");

rabbit = Rabbit();
fish = Fish();
hawk = Hawk();

print(rabbit.alive);
fish.swim().eat();
hawk.sleep();
