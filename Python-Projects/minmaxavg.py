from dataclasses import replace
from itertools import count
import random
import minmaxavg

melt_list = []
# minimum = 1000
# maximum = 999


def add_melt_num():
    for x in range(10):
        melt_temp = random.randint(0, 100)
        melt_list.append(melt_temp)


def find_min():
    print("The Max temp in Celsius is: ", min(melt_list))
    # for index in range(0, len(melt_list)):
    #     min_value = melt_list[index]
    #     if minimum < min_value:
    #         newMinimum = min_value
    #         print(newMinimum)


def find_max():
    print("The Max temp in Celsius is: ", max(melt_list))
    # for index in range(0, len(melt_list)):
    #     max_value = melt_list[index]
    #     if minimum < max_value:
    #         newMaximum = max_value
    #         print(newMaximum)


def findAvg():
    average = sum(melt_list)/len(melt_list)
    print("The Averge temp in Celsius is: ", average)
    # num = 0
    # count = len(melt_list)
    # for x in range(0, count):
    #     x_value = melt_list[x]
    #     melt_total = melt_total + x_value
    #     average = melt_total/len(melt_list)
