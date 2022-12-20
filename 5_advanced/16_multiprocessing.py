# multiprocessing = running tasks in parallel on different cpu cores, bypasses GIL used for thread
#                   multiprocessing = better for cpu tasks (heavy cpu usages)
#                   multithreading = better for  bound tasks (waiting around)

from multiprocessing import Process,  cpu_count
import time;

def counter(num):
    count = 0;
    while count < num:
        count += 1;

def main():
    print(cpu_count());
    cpuList = [Process(target=counter,args=(round(10000000000 / 10),)) for i in range(1, 10)];
    for cpu in cpuList:
        cpu.start();
        cpu.join();

    # a = Process(target=counter, args=(10000000000,))
    # a.start();
    # a.join();

    print('finished in'+ str(time.perf_counter()) + 'seconds');

if __name__ == '__main__':
    main();
