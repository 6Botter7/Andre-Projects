import random

lucky = 0

while lucky == 0:
    user_guess = []
    user1 = int(input(" Enter your first guess between 1 and 9   :"))
    while user1 < 1 or user1 > 9:
        print("PLEASE choose a number between 1 and 9  : ")
        user1 = int(input(" Enter your first guess between 1 and 9   :"))

    user2 = int(input(" Enter your second guess between 1 and 9  :"))
    while user2 < 1 or user2 > 9:
        print("PLEASE choose a number between 1 and 9  :")
        user2 = int(input(" Enter your second guess between 1 and 9   :"))

    user3 = int(input(" Enter your third guess between 1 and 9  :"))
    while user3 < 1 or user3 > 9:
        print("PLEASE choose a number between 1 and 9  :")
        user3 = int(input(" Enter your third guess between 1 and 9   :"))

    user_guess.append(user1)
    user_guess.append(user2)
    user_guess.append(user3)

    lot_nums = []
    lot1 = random.randint(1, 9)
    lot2 = random.randint(1, 9)
    lot3 = random.randint(1, 9)

    lot_nums.append(lot1)
    lot_nums.append(lot2)
    lot_nums.append(lot3)

    prizes = {
        0: 0,
        1: 10,
        2: 100,
        3: 1000,
        4: 1000000
    }

    winnings = 0

    def check_exact(user_guess, lot_nums):
        for i in range(0, len(lot_nums)):
            if user_guess[i] != lot_nums[i]:
                return False

        return True

    def check_occurance(user_guess, lot_nums):
        count = 0
        for i in range(0, len(lot_nums)):
            value = lot_nums[i]
            if value in user_guess:
                count += 1
                while value in user_guess:
                    user_guess.remove(value)

        return count

    print(f" Your guesses were{user_guess}")
    print(f"The Lotto numbers were {lot_nums}")

    exact = check_exact(user_guess, lot_nums)

    if exact == True:
        winnings == prizes[4]

    else:
        correct = check_occurance(user_guess, lot_nums)
        winnings = prizes[correct]

    print(f"You have won {winnings} !!")
    print("")

    opt = 0
    while opt == 0:
        play_again = input("Do you wanto play again ? \n y = yes, n = No  \n")
        if play_again == "y" or play_again == "Y":
            print("Here we go again..")
            opt += 1
            continue
        elif play_again == "n" or play_again == "N":
            print("Goodbye, till next time..")

            lucky += 1
            break
        else:
            print("Enter a valid selection  y/n  : \n ")

            play_again = input(
                "Do you wanto play again ? \n y = yes, n = No  \n")

    # play_again = input("Do you wanto play again ? \n y = yes, n = No  \n")      #working
    # if play_again == "y" or play_again == "Y":
    #     print("Here we go again..")
    #     continue
    # elif play_again == "n" or play_again == "N":
    #     print("Goodbye, till next time..")
    #     break
