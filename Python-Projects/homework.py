from dataclasses import replace
from stat import IO_REPARSE_TAG_APPEXECLINK


number = input("Enter an integer")


if type(number) == int:
    print("This is a integer")

elif type(number) == str:
    print("This is not an integer, try again")
# --------------------------------------------------

for i in range(1, 100):
    # while (i/i) == 1 and (i/i) != int:
    if (i/i) == 1 and (i/2) != int:
        print(i)
# --------------------------------------------------------

word = input("Insert word with e")


def e_word(word):
    for i in word:
        if i == "e":
            word = word.replace(i, "eee")
            print(word)


# -------------------------------------------------------


def y_word():
    x = 0
    while x == 0:
        u_input = input("Emter a word that starts with a 'Y'")
        if u_input[0] == "Y" or u_input[0] == "y":
            print("started with a 'y',  well done")
            x = 1

        else:
            print("Word does not begin with an 'Y', try again")


y_word()
