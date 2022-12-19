# super() = Function used to give access to the methods of a parent class.
#           Returns a temporary object of a parent class when used

class Rectangle:
    def __init__(self, length, width) -> None:
        self.length = length;
        self.width = width;

    def to_string(self):
        print("I am" + str(self));



class Square(Rectangle):

    def __init__(self, length, width) -> None:
        super().__init__(length, width);

    def area(self):
        return self.length * self.width;

    def to_string(self):
        super().to_string()



class Cube(Rectangle):

    def __init__(self, length, width, height) -> None:
        super().__init__(length, width);
        self.height = height;

    def area(self):
        return self.length * self.width * self.height;

square = Square(3 ,3);
cube = Cube(3, 3, 3);

print(square.area());
print(cube.area());

print(square.to_string());
print(cube.to_string());
