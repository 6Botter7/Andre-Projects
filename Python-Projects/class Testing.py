
from operator import truediv


my_string = "Hello Francois"

# prints from first number/index to last number entered/index
print(my_string[1:len(my_string)])
# Slices from index to 'letter' infront of number added(14)
print(my_string[10:14])
print(my_string[::3])  # Prints every (3rd) letter/value of the string

# string
francois = "the quick brown fox jumps over the lazy dog. the quick brown fox jumps over the lazy dog. the quick brown fox jumps over the lazy dog. the quick brown fox jumps over the lazy dog."

# starting index  :  ending index:  which index to print
print(francois[10:len(francois):2])

my_list = ["EEN", "TWEE", "DRIE", "VIER", 5, 6.0, my_string]

# First square is the item in the list, second [] is for the index of that item
print(my_list[1][1])

print(my_list[2])

lastList = ["fork", 5, "65", 'cat', 6.5]

print(lastList[3][2])
