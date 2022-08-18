import re
import os
import json
word_list = {"Hello": "Just a normal greeting",
             "Botter": "The Myth, the Man, the LEGENd",
             "Malan": "The Lil Cuzz of Botter"
             }

other_list = open("C:\Andre-Projects\Python-Projects\word_list.txt", 'r+')
list2 = open(
    "C:\Andre-Projects\Python-Projects\com_word_list.json", 'r+')

# print(word_list["Botter"])


def word_search(word_list):
    user_input = input("Please enter a word  :   ")
    w = open("C:\Andre-Projects\Python-Projects\word_list.txt", 'r+')
    print(word_list[user_input])


def word_search2(word_list):
    user_input = input("Please enter a word  :   ")
    w = open("C:\Andre-Projects\Python-Projects\com_word_list.json", 'r+')
    print(w[user_input])

# user_input = input("Please enter a word  :   ")
# if user_input == "Botter":
#     w = open("C:\Andre-Projects\Python-Projects\word_list.txt", 'r+')
#     print(w.read(user_input))

# elif user_input == "Joos":
#     w = open("C:\Andre-Projects\Python-Projects\word_list.txt", 'r+')
#     print(w.read(word_list["Joos"]))


# word_search(list2)
# word_search(other_list)
word_search2(list2)

# ==========================================================================================================

userWord = input("Please enter a word : ")

with open("C:\Andre-Projects\Python-Projects\com_word_list.json") as f:
    d = json.load(f)
    for word in d:
        if userWord == word:
            print(d[word])
