# Write a class that implements a rotating counter from 0 to 9. That is, the counter starts
# at 0, increments to 9, resets to 0 again, and repeats that cycle indefinitely. It should have
# increment()and reset()methods, the latter of which returns the current count then sets
# the count back to 0
from time import sleep


class Rotate:
    def __init__(self):
        self.timer = 0
        pass

    def add_time(self):
        while self.timer < 10:
            for i in range(0, 9):
                self.timer += 1
                sleep(1)
                print(self.timer)
            if self.timer == 9:
                self.timer = 0
                continue


starttimer = Rotate()

starttimer.add_time()
