# dictionary of keys and values loaded from json file
import json
import os
import re
dictionary = {
    "hello": "greeting",
    "world": "planet"
}


# extract the keys into an array for easy searching
keys = dictionary.keys()

# search function that will look at the keys and see if the key contains the phrase passed on


def search(phrase):
    result = filter(lambda item: item.__contains__(phrase), keys)
    return list(result)


# call search function with typed in phrase text
result = search("he")

# print result
print(result)


# Not that the result can be multiple items for example if you press "l" you will get both words back
# =========================================================================================================================================

characters = open("C:\Andre-Projects\Python-Projects\com_word_list.json")
d = json.load(characters)
key = characters.key()


def find_word(word):
    result = filter(lambda item: item.__contains__(word), key)
    return list(result)


outcome = find_word("Botter")

print(outcome)

# ===============================================================================================================================================?
f = open("C:\Andre-Projects\Python-Projects\word_list.txt", "r+")
# print(f.read())
search_word = input("Type word to search for: ")
if (search_word in f.read()):
    print(f.readline())
    print("Word found: ", search_word)
    print(f.readline())
else:
    print("Could not find word", search_word)

# ==================================================================================================================================================

people = open("C:\Andre-Projects\Python-Projects\com_word_list.json")
book = json.load(people)

print(book)
findW = input("Type word to search for: ")

for i in book:
    if i in book == findW:
        print(findW)
    else:
        print("Could not find word", findW)

print(book[0])

# person = book[findW]
# print(person)
# print(book[findW])

# =======================================================================


def from_file(file_path):
    file = open("C:\Andre-Projects\Python-Projects\com_word_list.json")
    data = json.load(file)
    file.close()
    return data


# u_i = input("Type word to search for: ")
# for i in data:
#     if i == u_i:
#         print(i)
#     else:
#         print("word not found")

def find_word1(word1):
    result = filter(lambda item: item.__contains__(word1), key)
    return list(result)


book1 = from_file("C:\Andre-Projects\Python-Projects\com_word_list.json")
outcome1 = find_word1("Botter")

print(outcome1)
