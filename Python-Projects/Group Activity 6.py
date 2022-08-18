import random
game_credits = 100

game_state = True
while game_state == True:
    game_cost = int(
        input("How much do you want to play?  (type '999' to quit):  "))

    if game_cost == 999:
        print("You quit the game. Cheers")
        break

    if game_credits == 0:
        print(
            "Whoops, unfortunately you are out of credits! Better luck next time! ")
        game_state = False
        break

    if game_cost > game_credits:
        print(
            f"You dont have that many credits, you only have {game_credits} left")

        continue

    random_num = random.randint(1, 9)
    user_guess = int(
        input("Enter a random guess between 1 and 9  :  "))

    print(
        f"The random n number was {random_num}, your number was {user_guess}")

    if user_guess == random_num:
        game_credits = game_credits + (game_cost*2)

        print(f"You now have {game_credits}   .")
        play = input("Do you want to play again ?  y/n :  ")

        valid = True
        while valid:
            if play == "y" or play == "Y":
                print("You chose to play")
                valid = False
                continue
                # break
            elif play == "n" or play == "N":
                print(f"Goodbye, You cashed out with {game_credits}")
                game_state = False
                break
            elif game_credits == 0:
                print(
                    "Whoops, unfortunately you are out of credits! Better luck next time! ")
                game_state = False
                break
            else:
                print("Please enter a valid option")
                play = input("Do you want to play again ?  y/n :  ")

    if user_guess != random_num:
        game_credits = game_credits - game_cost
        print(f"You now have {game_credits}")
        play = input(
            "That was wrong, do you want to play again?  y/n  :  ")
        valid = True
        while valid:
            if play == "y" or play == "Y":
                print("You chose to play again")
                valid = False
                continue

            elif play == "n" or play == "N":
                print(f"Goodbye, You cashed out with {game_credits}")
                game_state = False
                break
            else:
                print("Please enter a valid option")
                play = input("Do you want to play again ?  y/n :  ")
                continue

    if game_credits == 0:
        print(
            "Whoops, unfortunately you are out of credits! Better luck next time! ")
        game_state = False
        break
