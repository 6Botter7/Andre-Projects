import random
game_state = True
print('')
print('')
print(
    "---------------------------Welcome to the Rock, Paper, Scissors Game!------------------------")
print('')
while game_state:
    valid_move = False
    while not valid_move:
        possible_moves = ["rock", "paper", "scissors"]
        user_move = input("Do you choose ROCK, PAPER or SCISSORS   ?  ")
        if user_move in possible_moves:
            valid_move = True

        else:
            if not user_move != "rock" or user_move != "paper" or user_move != "scissors":
                print("Invalid move")
        # if not user_move in possible_moves:
        #     print("Please choose valid move")

    print(f"You chose {user_move.upper()}")
    computer_move = random.choice(possible_moves)
    print(f"The Computer Chose {computer_move.upper()}")

    if user_move.upper() == computer_move.upper():
        print(f"You both chose {user_move.upper()} , It is a TIE !!")

    elif user_move == "Rock" or user_move == "rock" and computer_move == "Paper" or computer_move == "paper":
        print(
            f"You LOSE !!! \n {computer_move.upper()}  beats {user_move.upper()}")

    elif user_move == "Rock" or user_move == "rock" and computer_move == "scissors":
        print(
            f"You WIN!!!  \n {user_move.upper()} wins {computer_move.upper()}!!")

    elif user_move == "Paper" or user_move == "paper" and computer_move == "rock":
        print(
            f"You WIN !!! \n {user_move.upper()} beats {computer_move.upper()} !!")

    elif user_move == "Paper" or user_move == "paper" and computer_move == "scissors":
        print(
            f"You LOSE !!! \n {computer_move.upper()} beats {user_move.upper()} !!")

    elif user_move == "Scissors" or user_move == "scissors" and computer_move == "paper":
        print(
            f"You WIN !!! \n {user_move.upper()} beats {computer_move.upper()} !!")

    elif user_move == "Scissors" or user_move == "scissors" and computer_move == "rock":
        print(
            f"You LOSE !!! \n {computer_move.upper()}  beats {user_move.upper()} !!")

    # else:
    #     print('Please choose ROCK, PAPER or SCISSORS')

    play_again = input("Do you want to play again?  y/n  ? ")
    if play_again == "y":
        continue
    elif play_again == "n":
        print("You chose to leave the game,  Goodbye!")
        game_state = False
        exit()
    else:
        print("Please enter a valid choice")
