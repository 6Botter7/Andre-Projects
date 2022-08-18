# Python-1
# Write a python program to print the following list in reverse order – by only making use of indexes.
# Do not use built-in functions like reverse().
# [5, 27, 18, 4, 8, 7, 2]

# Expected output: [2, 7, 8, 4, 18, 27, 5]

import random
from typing import MutableMapping
mlist = [5, 27, 18, 4, 8, 7, 2]
rlist = []
list_len = len(mlist)


def rev_print():
    # list_len = len(mlist)
    # while list_len > 0:
    for i in range(list_len-1, 0, -1):
        rlist.append(mlist[i])
        print(rlist)


        # if list_len == 0:
        #     print(rlist)
        #     break
rev_print()


# Python-2
# Write a python program to print the following list in ascending order – by only making use of indexes and your own logical code.
# Do not use built-in functions like sort().
# [5, 27, 18, 4, 8, 7, 2]

# Expected output: [2, 4, 5, 7, 8, 18, 27]

ascend_list = [5, 27, 18, 4, 8, 7, 2]

new_list = []
max = 0


def ascend():
    for i in range(len(ascend_list), 0, -1):
        if i > max:
            max == i
            new_list.insert(ascend_list[0], i)

        elif i < max:
            new_list.insert(ascend_list[1])
        print(new_list)


ascend()


# Python-3
# Write a python program to populate a list with 20 random numbers with values between 1 and 10.
# Print the number with the most occurrences in the list.
# Do not use built-in functions.
# -------------------------------------------------------------
# random_nums = []


# def populate():
#     for i in range(21):
#         random_nums.append(random.randint(1, 10))

#     print(random_nums)


# def occur():
#     for i in range(len(random_nums)):
#         for x in random_nums[i]:
#             if (random_nums[x]) == (random_nums[x]):
#                 v1 = 0
#                 v1 += 1

#     print(v1)


# populate()
# occur()
# --------------------------------------------------------------
random_nums = []
max_count = 0
vvalue = 0


# def populate():
#     global random_nums
for i in range(21):
    random_nums.append(random.randint(1, 10))

print(random_nums)


for i in random_nums:
    c = 0
    for num in random_nums:
        if num == i:
            c = c + 1
            if c > max_count:
                max_count = c
                vvalue = num


# populate()
print("now counting")
print(f"The most frequent number is {vvalue} and occured {max_count} times")

# Example list: [5, 3, 5, 10, 4, 7, 2, 1, 8, 7, 6, 3, 1, 6, 9, 2, 5, 8, 4, 10]
# Example output: The number 5 occurred 3 times.


# Python-4
# Write a python program to populate a list with 20 random numbers with values between 1 and 80.
# Find whether the list contains any duplicate elements.
# Print “true” and any values that appear at least twice in the list and print “false” if every element is distinct.
# Do not use built-in functions.
random_num = []


def populate():
    for i in range(21):
        random_num.append(random.randint(1, 80))

    print(random_num)


populate()

for i in range(len(random_num)):
    if i == random_num[i]:
        print("true")
    elif i != random_num[i]:
        print("false")


# Python-5
# Write a python program to populate a list with 20 random numbers with values between 1 and 40.
# Print the original list.
# Write code to remove all duplicate values from the original list and print the resulting list.
# Do not use built-in functions
random_no = []
no_dup_list = []
just_list = []


def populate():
    for i in range(21):
        random_no.append(random.randint(1, 40))

    print(random_no)


populate()

for item in random_no:
    if item not in no_dup_list:
        no_dup_list.append(item)


print(no_dup_list)


# for i in range(len(random_no)):
#     for i in range(len(random_no)):
#         for x in random_no:
#             if random_no[x] == random_no[x]:
#                 print(f"{x} is an equal")
#                 z = slice(random_no(i))
#                 no_dup_list.append(z)

#             elif random_no[x] != random_no[x]:
#                 just_list.append(i)
# if (random_no[i]) == (random_no[i]):
#     print(f"{i} is equal to a number {i}")
#     x = slice(random_no[i])
#     no_dup_list.append(x)
# elif random_no[i] != random_no[i]:
#     just_list.append(i)


print(no_dup_list)
print(just_list)
