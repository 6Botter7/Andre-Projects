bla = open("bla.txt", "w")
bla.write("I have no idea what to write.\n So I have decided just to write down words as they come to me.\n")

bla = open("bla.txt", "r")
print("")

print(bla.read())
print("")


# -------------------------------------------------------------------------------------
bla = open("bla.txt", "a")

bla.write("This is some more text.\n Still no idea what I am doing.\n")

bla = open("bla.txt", "r")
print(bla.read())
bla.close()

# -------------------------------------------------------------------------------------

# Not yet working.
blabla = bla

blabla = open("bla.txt", "r")
print(blabla.read())
# ----------------------------------------------------------------------------------


def call():
    in1 = input("Enter input 1  :  ")
    in2 = input("Enter input 2  :  ")
    in3 = input("Enter input 3  :  ")

    print(f"Input 1 was {in1}. \n Input 2 was {in2}.\n Input 3 was {in3}.")


call()
