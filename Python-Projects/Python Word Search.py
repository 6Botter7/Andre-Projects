# ************** NB **************
# dictionary.json is assumed in the same directory as the Python File...
# Execute this file from the same folder that the Python file is located in...
# ********************************************************************************

import json
from difflib import SequenceMatcher

open_book = True
print('')
print("This is a book of things and people in the Life of B O T T E R ")
print("Please enter the CORRECT spelling of one of the following names: ")
print(f"""            Botter    Malan     Tinashe 
            Joos      Elandre
            Michaela  Andre     Elmarie 
            Johan     Matthew   Hugo 
            Jolene    Morne     Patrick 
            Law       Beaufort  Leo 
            Beer      Pizza     Dog""")
while open_book:

    class WORD_SEARCH:
        def __init__(self, dictionary):
            print("")
            self.search_word = input("Type a word to search for: ______ ")

            file = open(dictionary)
            self.dictionary = json.load(file)
            file.close()

            self.keys = self.dictionary.keys()

            if self.search_word == "exit":
                print("Goodbye...")
                exit()

        def find_word(self):
            found = None
            for key in self.keys:
                if key == self.search_word:
                    print(
                        f"Exact match found !  : {key} = {self.dictionary[key]}")
                    found = key
                    break

                else:
                    ratio_for = SequenceMatcher(
                        None, key, self.search_word).ratio()
                    if ratio_for >= 0.7:
                        print(
                            f"Partial match found : {key} = {self.dictionary[key]}")
                        found = key
                        break

            if found == None:
                print("Unfortunately, no word of that spelling was found")
            # else:
            #     print(
            #         f"---------------- : {key} = {self.dictionary[key]}")

    result = WORD_SEARCH("dictionary.json")
    result.find_word()
