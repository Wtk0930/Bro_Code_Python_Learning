name = "wang TengKai";
numbers = "111111111";

# get the length of a string
print(len(name));
print( name.find("eng"));
# make first character capital and the rest lower case.
print( name.capitalize() );
print( name.upper() );
print( name.lower() );
print( name.isdigit(), numbers.isdigit() );
# to check if your string contains only alphabetical letters.
print( name.isalpha());
# count how many a character is in our string
print( name.count('a') );
# replace the characters in our string
print( name.replace('ang', "eeee"));
# display the string multiple times by multiplying that string by given number
print( name * 3 );


# slice the string
# [first:stop:step] including the first character

# way 1
first_name = name[0:4];
last_name = name[5:]
new_name = name[::2]
reversed_name = name[::-1];
print(first_name);
print(last_name);
print(new_name);
print(reversed_name);
# way 2
website = "http://google.com";
# the negative index gets the position from the end.
slice = slice(7, -4);
print(website[slice]);




# str.format() = optional method that gives users more control when displaying output
print("The {} jumped over the {}".format("cow","moon"));
# positional argument
print("The {1} jumped over the {0}".format("cow","moon"));
print("The {1} jumped over the {1}".format("cow","moon"));

# keyword argument
print("The {animal} jumped over the {item}".format(animal="cow", item="moon"));

name = "Bro";

print("Hello, my name is {}".format(name));
# add padding to a value
print("Hello, my name is {0:10}，1111".format(name));
# align your value
print("Hello, my name is {name:<10}，1111".format(name=name));
print("Hello, my name is {:>10}，1111".format(name));
print("Hello, my name is {:^10}，1111".format(name));

# format some numbers
number1 = 3.1415926;
number2 = 1000;

# use two decimal places
print("The number pi is {:.2f}".format(number1));
# insert a comma to the number
print("The number pi is {:,}".format(number2));
# display your number as binary
print("The number pi is {:b}".format(number2));
# display your number as octal number
print("The number pi is {:o}".format(number2));
# display your number as hexadecimal number
print("The number pi is {:x}".format(number2));
# display the number in scientific notation
print("The number pi is {:e}".format(number2));
