class Car:

    def turn_on(self):
        print("turn on");
        return self;

    def drive(self):
        print("drive");
        return self;

    def brake(self):
        print("brake");
        return self;

    def turn_off(self):
        print("turn_off");
        return self;

car = Car();

car.turn_on().drive().brake().turn_off();
