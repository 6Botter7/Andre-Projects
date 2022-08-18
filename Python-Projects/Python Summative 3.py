import random
print("***   Welcome to TICK-TACK-TOE  ***")
active_game = True

while active_game == True:

    def print_board(board):
        print(board[0] + " | " + board[1] + " | " + board[2])
        print("---------")
        print(board[3] + " | " + board[4] + " | " + board[5])
        print("---------")
        print(board[6] + " | " + board[7] + " | " + board[8])

    user = "X"
    computer = "O"
    board = ["-", "-", "-",
             "-", "-", "-",
             "-", "-", "-"]

    explained_board = ["1", "2", "3",
                       "4", "5", "6",
                       "7", "8", "9"]

    print("")
    print("This is the board")
    print("")
    print(print_board(board))
    print("")
    print(print_board(explained_board))
    print("")
    print("""    You will be 'X' 
    The Computer will be 'O'! 
            
            """)

    def player_move(board):
        print("Please select a position to play between 1 to 9  ?")
        valid = False
        while valid == False:

            move = int(input("===>  : "))

            if board[move-1] == "-":
                board[move-1] = user
                valid = True
                continue

            else:
                print("Unfortunately, the computer is already at that position")

            # while move != 1 or move != 2 or move != 3 or move != 4 or move != 5 or move != 6 or move != 7 or move != 8 or move != 9:
            #     if move == str():
            #         print("Please select a NUMBER to play between 1 to 9?")
            #         break
            #     else:
            #         print("Please select a NUMBER between 1 and 9")
            #         break

            # move = int(input("===>  : "))
            # if board[move-1] == "-":
            #     board[move-1] = user

        print(print_board(board))

    def computer_move(board):
        not_played = True
        while not_played:

            move = random.randint(1, 9)
            if board[move-1] == "-":
                board[move-1] = computer
                not_played = False
            # else:
            #     print("ooopsiee")
            #     move = random.randint(1, 9)
            #     if board[move-1] == "-":
            #         board[move-1] = computer

            print(print_board(board))

    def check_win(board):
        winner = None
        while winner:
            # ROWS ONLY
            if board[0] == "X" and board[1] == "X" and board[2] == "X":
                print("You WIN!")
                winner == 1
                # exit()

            elif board[0] == "O" and board[1] == "O" and board[2] == "O":
                print("You LOSE! The COMPUTER has WON !")
                winner == 1
                # exit()

            elif board[3] == "X" and board[4] == "X" and board[5] == "X":
                print("You WIN!")
                winner == 1
                # exit()

            elif board[3] == "O" and board[4] == "O" and board[5] == "O":
                print("You LOSE! The COMPUTER has WON !")
                winner == 1
                # exit()

            elif board[6] == "X" and board[7] == "X" and board[8] == "X":
                print("You WIN!")
                winner == 1
                # exit()

            elif board[6] == "O" and board[7] == "O" and board[8] == "O":
                print("You LOSE! The COMPUTER has WON !")
                winner == 1
                # exit()

            # Collumns ONLY
            elif board[0] == "X" and board[3] == "X" and board[6] == "X":
                print("You WIN!")
                winner == 1
                # exit()

            elif board[0] == "O" and board[3] == "O" and board[6] == "O":
                print("You LOSE! The COMPUTER has WON !")
                winner == 1
                # exit()

            elif board[1] == "X" and board[4] == "X" and board[7] == "X":
                print("You WIN!")
                winner == 1
                # exit()

            elif board[1] == "O" and board[4] == "O" and board[7] == "O":
                print("You LOSE! The COMPUTER has WON !")
                winner == 1
                # exit()

            elif board[2] == "X" and board[5] == "X" and board[8] == "X":
                print("You WIN!")
                winner == 1
                # exit()

            elif board[2] == "O" and board[5] == "O" and board[8] == "O":
                print("You LOSE! The COMPUTER has WON !")
                winner == 1
                # exit()

            # Diagonal
            elif board[0] == "X" and board[4] == "X" and board[8] == "X":
                print("You WIN!")
                winner == 1
                # exit()

            elif board[0] == "O" and board[4] == "O" and board[8] == "O":
                print("You LOSE! The COMPUTER has WON !")
                winner == 1
                # exit()

            elif board[2] == "X" and board[4] == "X" and board[6] == "X":
                print("You WIN!")
                winner == 1
                # exit()

            elif board[2] == "O" and board[4] == "O" and board[6] == "O":
                print("You LOSE! The COMPUTER has WON !")
                winner == 1
                # exit()

        if winner == 1:
            another_game = input(
                "Do you want to play again ?  y/n ?   :  ")
            if another_game.lower() == "y":
                break
            elif another_game.lower == "n":
                print("Goodbye")
                exit()

    def check_If_Tie(board):
        if "-" not in board:
            print("It is a tie!")
            print("")
            print("Try again later!")
            # another_game = input("Do you want to play again ?  y/n ?   :  ")
            # if another_game.lower() == "y":
            #     continue
            # elif another_game.lower == "n":
            #     print("Goodbye")
            exit()

    while active_game == True:
        # print_board(board)
        player_move(board)
        check_win(board)
        check_If_Tie(board)

        computer_move(board)
        check_win(board)
        check_If_Tie(board)

        if active_game == False:
            break


# while True:
#                 if play_again == "y":
#                     break

#                 else:
#                     print("You chose to leave the game. GOODBYE !")
#                     exit()

# ===============================================================================================

#game_state = True
# print('')
# print('')
# print(
#     "---------------------------Welcome to the Rock, Paper, Scissors Game!------------------------")
# print('')
# while game_state:

# play_again = input("Do you want to play again?  y/n  ? ")
#     if play_again == "y":
#         continue
#     elif play_again == "n":
#         print("You chose to leave the game,  Goodbye!")
#         game_state = False
#         exit()
#     else:
#         print("Please enter a valid choice")


# elif board[0] == "O" and board[4] == "O" and board[8] == "O":
#                 print("You LOSE! The COMPUTER has WON !")
#                 exit()


# another_game = input(
#                     "Do you want to play again ?  y/n ?   :  ")
#             if another_game.lower() == "y":
#                 continue
#             elif another_game.lower == "n":
#                 print("Goodbye")
#                 exit()
