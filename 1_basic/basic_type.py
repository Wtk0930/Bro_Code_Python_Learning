print("I love English");
print("It's really fabulous");

# variable
name = "Bro";
full_name = name + name;

# type function can check the type of a variable
print( type(name) );



age = 21;
age += 1;
# it will cause a error, for the operation can only be done between two operators which have the same type
# age += '11';

# str() can convert a variable to a string
print(type(age), type(str(age)));

# float
height = 250.5;
print(height, type(height));

# boolean
human = False;
print(human, type(human));


# multiple assignment
a, b, c = 11, "22", 123412.222;
print(a, b, c);
