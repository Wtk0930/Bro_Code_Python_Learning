# module = a file containing python code.May contain functions, classes, etc.
# used with modular programing, which is to operate a program into parts.

# best practice more safer
import messages as msg;
# don't use it in big programs to avoid the functions which have the same names in other modules
# from messages import hello, bye;
from messages import *;

# to list the available modulesin python
help("modules");



msg.hello();
msg.bye();

hello();
bye();
