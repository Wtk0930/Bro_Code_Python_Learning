# Duck typing = concept where the class of an object is less important than the methods / attributes
#               class type is not checked if minimum methods / attributes are present
#               "if it walks like a duck, and it quacks like a duck, then it must be a duck"

class Duck:

    def walk(self):
        print("this duck is walking")

    def talk(self):
        print("this duck is quacking");

class Chicken:

    def walk(self):
        print("this chicken is walking")

    def talk(self):
        print("this chicken is clucking");

class Person:

    def catch(self, duck:Duck):
        duck.walk();
        duck.talk();
        print("You caught the critter");

duck = Duck();
chicken = Chicken();
person = Person();

person.catch(duck);

# because the Chicken class has the similar attributes / methods as the Duck class
# so you can also pass chicken instance to the function
person.catch(chicken);
