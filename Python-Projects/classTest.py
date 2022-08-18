from cmath import nan
from multiprocessing.sharedctypes import Value
from re import I
import string
import random
import imp
import math
from tabnanny import NannyNag
from tokenize import Number
from xml.dom.pulldom import CHARACTERS
userNo = float(input("Enter your number"))


def guess():
    attempt = float(input("enter your guess"))
    if attempt != userNo:
        print("Haha try again!!")
        guess()
    elif attempt == userNo:
        print("Well done, You got it right")
        return print(userNo)


guess()
# -----------------------------------------------------------
credits = float(input("How many Credits have you taken ? "))

if credits <= 23:
    print("You are still a Freshman!!")

elif credits > 23 and credits <= 53:
    print("You are a Sophomore")

if credits > 53 and credits <= 83:
    print("You are a Junior")

elif credits > 83:
    print("You are a Senior!")

# ------------------------------------------------------------

mark = float(input("Enter your mark"))

if mark > 90:
    print("A")

elif mark < 90 and mark > 80:
    print("B")

elif mark < 80 and mark > 70:
    print("C")

elif mark < 70:
    print("You Fail!!")
# -------------------------------------------------------------


def passwordGen():
    newPass = ''.join(random.choice(CHARACTERS) for i in range(0, 16))
    newString = newPass
    return newString


def myPassword():
    print("Your new password is : ")
    print(passwordGen())
# ----------------------------------------------------------------------


def age_Rate():
    age = float(input("Enter your AGE"))
    if age >= 18:
        print("Your age rating is 'A' ")

    elif age < 18 and age >= 13:
        print("Your age rating is'T' ")

    elif age <= 12:
        print("Your age rating is 'C' ")

    elif age == int:
        print("You gave no age, you have a rating of 'C' ")
    elif age == age:
        print("You gave no age, you have a rating of 'C' ")
# ----------------------------------------------------------


vowels = ["a", "e", "i", "o", "u"]
word = input("Enter your Word here")

for x in range(0, len(vowels), 1):
    for z in range(0, len(word), ):
        if word[z] == vowels[x]:
            print("This word contains a vow")  # Did not complete
# -------------------------------------------------------------

randomWord = input("Enter a random word")


def transform():
    print(randomWord[1])


# -------------------------------------------------------------
word = input("enter your own word")

for i in range(len(word)):

    if(word == "a" or word == "e" or word == "u" or word == "i" or word == "A" or word == "E" or word == "U" or word == "I"):

        print("the given character, word, is a vowel")


else:
    print("the given character, word, is invalid")

# -----------------------------------------------------------------
fo = open("Williams-a rich text format Life Skills.docx", "r+")

print("File read", fo.name)
fo.close()

fo = open("Williams-a rich text format Life Skills.docx", "a")

fo.write("Hello,How are you? \n Good, thanks for asking!\n ")

fo.close()

fo = open("Williams-a rich text format Life Skills.docx", "r+")

print(fo.readlines())
