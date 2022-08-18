import random
import string

passwordNum = int(input("How many passwords do you need?"))
passTotal = 0

lower = string.ascii_lowercase
upper = string.ascii_uppercase
num = string.digits
special = string.punctuation

while passTotal != passwordNum:

    if input == quit:  # quit statement
        quit()

    print("let's get you a unique password ")  # opening statemnet
    pLength = int(
        input("\n How many characters do you want your password to be ? : "))
    for i in range(0, passwordNum):
        print(' ')

        all = lower + upper + num + special
        temp = random.sample(all, pLength)
        password = "".join(temp)
        # passwordNum += 1

        print(' ')
        print(f'' "Password", i, ": ", password)
        passTotal += 1
        if passTotal == passwordNum:
            break
