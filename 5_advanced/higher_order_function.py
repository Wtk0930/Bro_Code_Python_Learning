# Higher Order Function = a function that either:
#                           1. accepts a function as argument
#                                   or
# `                         2. returns a function
#                           (in python, functions are also treated as objects)


# case 1
def loud(text):
    return text.upper();

def quiet(text):
    return text.lower();


def hello(function):
    text = function("Hello");
    print(text);

hello(loud);
hello(quiet);


# case 2
# just like the closure function
z = 10;
def divisor(x):
    def dividend(y):
        return y / x * z;
    return dividend;

divide = divisor(2)
print(divide(10));
