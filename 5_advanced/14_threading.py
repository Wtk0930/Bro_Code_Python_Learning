# thread = a flow of execution.Like a separate order of instructions,
#           However each thread takes a turn running to achieve concurrency
#           GIL = (global interpreter lock)
#           allows only one thread to hold the control of the python interpreter

# cpu bound = program/task spends most of it's time waiting for internal events (cpu intensive)
#               use multiprocessing

# io bound = program/task spends most of it's time waiting for external events (user input, web scraping)
#               use multiprocessing

import threading;
import time;

# Return the number of Thread objects currently alive.
print(threading.active_count());
# Return a list of all Thread objects currently alive.
print(threading.enumerate())


def eat_breakfast():
    time.sleep(3);
    print('you ate breakfast');

def drink_coffee():
    time.sleep(4);
    print('you drank coffee');

def study():
    time.sleep(5);
    print('you finish studying');


# cost 12 seconds
# eat_breakfast();
# drink_coffee();
# study();

# create a thread
x = threading.Thread(target=eat_breakfast, args=());
x.start();

# create a thread
y = threading.Thread(target=drink_coffee, args=());
y.start();

# create a thread
z = threading.Thread(target=study, args=());
z.start();


# Wait until the thread terminates.
x.join()

# Return the number of Thread objects currently alive.
print(threading.active_count());
# Return a list of all Thread objects currently alive.
print(threading.enumerate())
# Performance counter for benchmarking. the cost for the current thread
print(time.perf_counter())
