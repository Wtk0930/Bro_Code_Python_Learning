# walrus operator :=

# new to Python 3.8
# assignment expression aka walrus operator
# assigns values to variables as part of a larger expression


# case 1
# happy = True;
# print(happy);
# you can also do the same thing as the code above by
print(happy := True);




# case 2
# foods = list();
# while True:
#     food = input("What food do you like?:")
#     if food == "quit":
#         break;
#     foods.append(food);
foods = list();
while  food := input("What food do you like?:") != "quit":
    foods.append(food);
