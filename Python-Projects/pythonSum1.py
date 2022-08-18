from difflib import SequenceMatcher
import json
from enum import Enum

# create a enum to define what kind of search we want to perform.
# it can be either exact or partial.


class Match(Enum):
    EXACT = 1
    PARTIAL = 2


# search class used to perform the searches.
# it loads the json on startup and sets a dictionary attribute that we will perform the search on.
# we pass the dictionary on to the constructor so that it has a bit more flexability around what dictionary to use.

# 1. use json to define key value pairs
# 2. the key is what I search on, the value is the definition
# 3. load json file and exact the keys using the ".keys()" function
# 4. loop through keys and check if it matches search

class Search:

    def __init__(self, dictionary):
        # load the file and get the content from it as json.
        # remember to close the file again
        file = open(dictionary)
        self.dictionary = json.load(file)
        file.close()

        # get the keys from the json so that we can search against it.
        self.keys = self.dictionary.keys()

    # perform a search and define what to search for id if it should be exact or partial

    def find(self, search_text, match):

        return self.find_exact(search_text) if match == Match.EXACT else self.find_partial(search_text)

    # how to perform an exact search where the word must match 100%
    def find_exact(self, search_text):
        self.search_text = input("Search text: ")
        for key in self.keys:
            if key == self.search_text:
                return self.dictionary[key]

            elif self.search_text != self.dictionary[key]:
                s_1 = self.dictionary[key]
                s_2 = self.search_text
                if SequenceMatcher(a=s_1, b=s_2).ratio() > 0.7:
                    print(
                        f"Did you maybe mean {self.dictionary[key]} ? \n Please Type that word again with CORRECT spelling. ")

                # print(SequenceMatcher(a=s_1, b=s_2).ratio())

        # nothing was found return None
        return print("No match found for " + search_text)

    # performa a partial search so that you don't need to define the entire word but it will return all items where the
    # word contains the text you have defined

    # def find_similar_word(self, search_text):
    #     result = []
    #     if search_text != self.dictionary[self.key]:                   # test
    #             s_1 = self.dictionary[self.key]
    #             s_2 = search_text
    #             if SequenceMatcher(a=s_1, b=s_2).ratio() > 0.7:
    #                 print(
    #                     f"Did you maybe mean {self.dictionary[self.key]} ? \n Please Type that word again with CORRECT spelling. ")

    # def find_partial(self, search_text):

    #     result = []
    #     for key in self.keys:
    #         if key.__contains__(search_text):
    #             result.append("{}: {}".format(key, self.dictionary[key]))

    #     return result


search = Search("C:\Andre-Projects\Python-Projects\dictionary.json")

# replace search text with actual input
print("**** exact match ****")
results = search.find('name', Match.EXACT)
print(results)


# print("**** partial match ****")
# results = search.find("l", Match.PARTIAL)
# print(results)

# print("**** partial match ****")
# results = search.find("hel", Match.PARTIAL)
# print(results)
