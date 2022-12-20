# daemon thread = a thread runs in the background, not important for programs to run
#                 your program will not wait for daemon to complete before exiting
#                 non-daemon threads cannot normally be killed, stay alive until task is complete
#
#                 ex. background tasks, garbage collection,waiting for input, long running processes

import threading;
import time;

def timer():
    print();
    count = 0;

    while True:
        time.sleep(1);
        count += 1;
        print('logged in for: ', count, 'seconds');

# a daemon thread can be killed automatically
x = threading.Thread(target=timer, daemon=True);

# x.setDaemon(True);
# print(x.isDaemon());
x.start();

answer = input('Do you wish to exit');
