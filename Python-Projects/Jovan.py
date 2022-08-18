import random

randomm = 0

while randomm == 0:
    userguess = []
    print("Guess 3 random number and sand a chance to win!!")
    user1 = int(input(" Enter your first number between 1 and 9   :"))
    user2 = int(input(" Enter your second number between 1 and 9  :"))
    user3 = int(input(" Enter your third number between 1 and 9  :"))

    def checkxa(user_guess, lottNumber):
        for x in range(0, len(lottNumber)):
            if userguess[x] != lottNumber[x]:
                return False

        return True

    def checkoccurance(lottNumber, userguess):
        tel = 0
        for x in range(0, len(lottNumber)):
            value = lottNumber[x]
            if value in userguess:
                tel += 1
                while value in userguess:
                    userguess.remove(value)

        return tel

    userguess.append(user1)
    userguess.append(user2)
    userguess.append(user3)

    MonPrize = {
        0:  0,
        1:  10,
        2:  100,
        3:  1000,
        4:  1000000
    }

    lottNumber = []
    lott1 = random.randint(1, 9)
    lott2 = random.randint(1, 9)
    lott3 = random.randint(1, 9)
    lottNumber.append(lott1)
    lottNumber.append(lott2)
    lottNumber.append(lott3)

    win = 0
    xa = checkxa(userguess, lottNumber)

    print(f"{userguess} was the number you guessed")
    print(f"{lottNumber} was the lotto number")

    if xa == True:
        win == MonPrize[4]

    else:
        correct = checkoccurance(userguess, lottNumber)
        win = MonPrize[correct]

    print(f"You just won {win} \n Congratulations")

    print(" ")

    UserC = input("Wanna play again ? \n y = yes, n = No  \n")
    if UserC == "Y" or UserC == "y":
        print("Next round...")

    elif UserC == "N" or UserC == "n":
        print("Thank you for playing \n Goodbey ")
        break
