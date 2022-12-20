# python interpreter sets special variables, one of which is __name__
# Python will assign the __name__ variable a value of '__main__' if it's
# the initial module being run
#  reason: Module can be run as a standalone program or can be imported and used by other modules

print(1)
print(__name__);
