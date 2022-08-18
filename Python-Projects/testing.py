from re import I
import re
from turtle import st
from unicodedata import name


lys = []

lys.append(20)
lys.append("Hello")  # .append is to add to A LIST
# Only one element at a time

print(lys)
# -------------------------------------------------------------

# Check to see if a number is Odd or Even
number = float(input("Enter a value"))


if (number % 2) == 0:
    print("The number is even")
else:
    print("The provided number is odd")

# -------------------------------------------------------------


for num in range(3):

    num1 = float(input("Number 1"))**2
    num2 = float(input("Number 2"))**2
    num3 = float(input("Number 3"))**2

    print(num1, num2, num3)
    break
 # --------------------------------------------------------------

userNo = float(input("Enter your number"))


def guess():
    attempt = float(input("enter your guess"))
    if attempt != userNo:
        print("Haha try again!!")  # NOT WORKING
        attempt
    elif attempt == userNo:
        print("Well done, You got it right")
        return print(userNo)


# -------------------------------------------------------
i = 0

while i < 100:
    print(i)
    i = i + 1


# for loops to run a certain amount of times. Exact number or duration

# While loops runs(and continues) when/when a certain condition is true or False.
# --------------------------------------------------------------------
attempts = 0  # Creates a Variable and gives a value of 0
# Creates a while loop and says : While the value of attempts(above declared variable), is less than 3, continue the loop
while attempts < 3:
    # While the loop is running and attempts are still less tan 3, create a new variable called "number", and number is equal to the input of the user (int(input("some string")))
    number = int(input("Enter a number"))
    # Create another new variable, called numberSquare, and that variable is equal to the user's input squared(**2)
    numberSquare = number**2
    # After this is done, update the attempt value by adding 1, So attempts will now be 1(attempts = 1). This will run over and over umtil attempts(the variable), is equal to 3
    attempts = attempts + 1
    # Then we print the value of numberSquare (User input **2)
    print(numberSquare)
# -------------------------------------------------------------------------------------------------
# note the indentation, all the above is in the while loop, the while loop runs until attempts are less than 3, then stops.
# the Print is a new funtion we call, outside the loop, so when the loop is done, please print this (In this case it is the words in the string"")
print("the loop is done!")

# prompt the user 3 times, after 3 times break loop and print
# ------------------------------------------------------------
tries = 0  # We create a variable called "tries", with a value of 0

# We start our for loop. We basically say 'i' is equal to 3 times, so the loop will run for 3 times.
for i in range(3):
    # in the for loop, create a new variable called "nom", and nom is equal to the input pf the user (input funtion)
    nom = int(input("enter a nimber to be squared"))
    # we create another variable, "nomS", and this variable is equal to the user's input squared(**2)
    nomS = nom**2
    print(nomS)  # please print the value of nomS
    # After the print please update the variable called "tries" (above, in the beginning),by adding 1
    tries = tries + 1
    if tries == 3:  # then we write an If statement inside the For loop. The statement says : If the variable called "tries", is equal to 3, then...:
        # Print the value of the variable called tries, dont worry about the 'f' infront of the string or the {}curly brackets, we will cover that later. You can just say: print(tries)
        print(f"Your total tries were {tries}")
        print("Your loop is done")  # Print the string("") "Your loop is done"
# ---------------------------------------------------------
for i in range(1500, 2700):
    if (i % 7 == 0) and (i % 5 == 0):
        print(i)
# ----------------------------------------------
for i in range(1500, 2700):
    if (i % 7 == 0) or (i % 5 == 0):
        print(i)
# --------------------------------------------------

naaam = "Malan"


def values(x, y):
    print(f"The value of x is {x} and the value of y is {y}")
    return values


print(f"{8*8} is basically 8x8")

values(6, 9)
# print("My name is", naaam)
print(f"My name is {naaam}")


def subtract(x, y):
    print(x-y)

# ------------------------------------------------------
# File handling..


file = open("Williams.txt", "a",)

print(file.name)
print(file.mode)
file.write("Hello World I am File")


file = open("Williams.txt", "r+")

str = file.read(7)

print(str)
file.close()


demo = open("demofile.txt", "a")
demo.write("This file is for \n testing Purposes \n Good Luck.")

demo = open("demofile.txt", "r")
red = demo.read()

print(red)

demo = open("Williams.txt", "w+")
pos = demo.tell()
print(pos)

seek = demo.seek(0, 0)

demo.close()
