import car;

car_1 = car.Car("Chevy", "Corvette", 2021, "blue");
car_2 = car.Car("Ford", "Mustang", 2022, "red");

car_1.drive();
car_1.stop();
car_2.drive();
car_2.stop();

# access class variable
print(car.Car.wheels);
# access instance variable
print(car_1.color);

car.Car.wheels = 2;
print(car_1.wheels);
print(car_2.wheels);
