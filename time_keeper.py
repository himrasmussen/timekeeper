#!/usr/bin/env python3
import sys
import time
import shelve

class TimeKeeper:

    def __init__(self):
        time_keeper_shelf.setdefault(sys.argv[1], 0)
        self.work_time = time_keeper_shelf[sys.argv[1]] #is int not key

    def running(self):
        self.start_time = time.time()
        self.prompt = input("Press 'enter' to stop time.")
        self.run_time = int(round(time.time() - self.start_time, 0))
        time_keeper_shelf[sys.argv[1]] += self.run_time
        self.stopped()

    def stopped(self):
        self.print_time()
        self.prompt = input("Press 'enter' to start time.")
        self.running()

    def print_time(self):
        self.get_h_m()
        print("Worked for{}:{}:{}.\n".format(self.h, self.m, self.s))
        print("Worked for: {} seconds.".format(time_keeper_shelf[sys.argv[1]]))

    def get_h_m(self):
        self.seconds = time_keeper_shelf[sys.argv[1]]
        self.m, self.s = divmod(self.seconds, 60)
        self.h, self.m = divmod(self.m, 60)

    def subtract_time(self):
        pass

    def run(self):
        print("Initializing.")
        self.print_time()
        self.running()


if __name__ == "__main__":
    print("Hello")
    time_keeper_shelf = shelve.open("time_keeper")
    if "times" in sys.argv[1]:
        for key, value in time_keeper_shelf.items():
            print("{}: {}".format(key, value))
    elif len(sys.argv) == 2:
        my_time_keeper = TimeKeeper()
        my_time_keeper.run()

    elif "add" in sys.argv[2]:
        try:
            time_keeper_shelf[sys.argv[1]] += int(sys.argv[3])
        except:
            print("Bad input.")

    elif len(sys.argv) == 3 and "del" in sys.argv[1]:
        del time_keeper_shelf[sys.argv[2]]
        print("TimeKeeper for {} deleted.".format(sys.argv[2]))
    elif len(sys.argv) == 3 and "get" in sys.argv[1]:
        TimeKeeper().get_time()
