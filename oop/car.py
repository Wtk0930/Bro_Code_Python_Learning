class Car:

    wheels = 4;  # class variable


    def __init__(self, make, model, year, color) -> None:
        self.make = make;    # instance variable
        self.model = model;  # instance variable
        self.year = year;    # instance variable
        self.color = color;  # instance variable


    # self refers to the object that use this method
    # note: when you call the method using "object.drive", the object itself will be pass to the function  as a argument automatically
    def drive(self):
        print("this {} is driving".format(self.model));

    def stop(self):
        print("this {} is stopped".format(self.model));
