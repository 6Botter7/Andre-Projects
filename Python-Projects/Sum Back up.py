import json
from tkinter import W
from difflib import SequenceMatcher

open_book = True
while open_book:
    print('')
    print("This is a book of things and people in the Life of B O T T E R ")
    print("Please enter the correct spelling of on of the following names: ")
    print(f"""              Botter    Malan     Tinashe 
              Joos      Elandre
              Michaela  Andre     Elmarie 
              Johan     Matthew   Hugo 
              Jolene    Morne     Patrick 
              Law       Beaufort  Leo 
              Beer      Pizza     Dog""")

    class WORD_SEARCH:
        def __init__(self, dictionary):
            print("-**************  This is a dictionary  **************_")
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
            for key in self.keys:
                if key == self.search_word:
                    print("")
                    print(f"This word is :   {self.dictionary[key]}")
                    print("")

                # elif key != self.search_word:
                #     i = input(
                #         f"Did you mean : {self.dictionary[key]}  ?     y/n:  ")
                #     if (i == "y"):
                #         print(self.dictionary[key])
                #     elif (i == "n"):
                #         exit()

                else:
                    # 1. Get the dictionary word /

                    # 2. Get sequence match for dictionary and search word

                    ratio_for = SequenceMatcher(key, self.search_word).ratio()

                    # 3. If the match is > than 70% , it = sucess
                    if ratio_for >= 0.7:
                        print(
                            f"closest match found was {key} = {self.dictionary[key]}")

                    # 4. else , Keep searching

                    # if key != self.dictionary[key]:
                    #     print("Looks like there is a spelling error !!")

                    # # if not self.search_word in self.dictionary:
                    #     s_1 = self.dictionary[key]
                    #     s_2 = self.search_word
                    #     if SequenceMatcher(a=s_1, b=s_2).ratio() >= 0.8:
                    #         print(
                    #             f"Did you maybe mean {self.dictionary[key]} ? \n Please Type that word again with CORRECT spelling. ")
                    #         break
                    #     else:
                    #         print(
                    #             "Sorry, there was no word found of this spelling  : ", self.search_word)
                    #         break

    result = WORD_SEARCH("C:\Andre-Projects\Python-Projects\dictionary.json")
    result.find_word()
