def hello(name:str):
    print("hello! " + name);
    print("have a nice day!");

hello("wtk");

# keyword arguments
def hello_2(first: str, middle: str, last: str):
    print(first,middle,last);
# call the function through passing the keyword
hello_2(last="k", first="w", middle="t");





# *args = parameter that will pack all arguments into a tuple
# useful so that a function can accept a varying amount of arguments
def add(*numbers):
    all_sum = 0;
    stuff = list(numbers);
    for i in stuff:
        all_sum += i;
    return all_sum;

print(add(1, 2, 5));





# **kwargs = parameter that will pack all arguments into dictionary
# useful so that a function can accept a varying amount of keyword arguments
def hello_3(**name):
    print("Hello " + name.get("first") + " " + name.get("last"));

hello_3(first="w", last="tk");
