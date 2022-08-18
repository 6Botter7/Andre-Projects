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
            try:
                move = int(input("===>  : "))

                if board[move-1] == "-":
                    board[move-1] = user
                    valid = True
                    continue
            except ValueError:
                print('Sorry, please enter a NUMBER between 1 and 9')

            except IndexError:
                print('Sorry, please enter a NUMBER between 1 and 9')

            else:
                print("Unfortunately, the computer is already at that position")


        print(print_board(board))

    def computer_move(board):
        not_played = True
        while not_played:

            move = random.randint(1, 9)
            if board[move-1] == "-":
                board[move-1] = computer
                not_played = False


            print(print_board(board))

    def check_win(board):
        # ROWS ONLY
        if board[0] == "X" and board[1] == "X" and board[2] == "X":
            print("You WIN!")
            exit()

        elif board[0] == "O" and board[1] == "O" and board[2] == "O":
            print("You LOSE! The COMPUTER has WON !")
            exit()

        elif board[3] == "X" and board[4] == "X" and board[5] == "X":
            print("You WIN!")
            exit()

        elif board[3] == "O" and board[4] == "O" and board[5] == "O":
            print("You LOSE! The COMPUTER has WON !")
            exit()

        elif board[6] == "X" and board[7] == "X" and board[8] == "X":
            print("You WIN!")
            exit()

        elif board[6] == "O" and board[7] == "O" and board[8] == "O":
            print("You LOSE! The COMPUTER has WON !")
            exit()

        # Collumns ONLY
        elif board[0] == "X" and board[3] == "X" and board[6] == "X":
            print("You WIN!")
            exit()

        elif board[0] == "O" and board[3] == "O" and board[6] == "O":
            print("You LOSE! The COMPUTER has WON !")
            exit()

        elif board[1] == "X" and board[4] == "X" and board[7] == "X":
            print("You WIN!")
            exit()

        elif board[1] == "O" and board[4] == "O" and board[7] == "O":
            print("You LOSE! The COMPUTER has WON !")
            exit()

        elif board[2] == "X" and board[5] == "X" and board[8] == "X":
            print("You WIN!")
            exit()

        elif board[2] == "O" and board[5] == "O" and board[8] == "O":
            print("You LOSE! The COMPUTER has WON !")
            exit()

        # Diagonal
        elif board[0] == "X" and board[4] == "X" and board[8] == "X":
            print("You WIN!")
            exit()

        elif board[0] == "O" and board[4] == "O" and board[8] == "O":
            print("You LOSE! The COMPUTER has WON !")
            exit()

        elif board[2] == "X" and board[4] == "X" and board[6] == "X":
            print("You WIN!")
            exit()

        elif board[2] == "O" and board[4] == "O" and board[6] == "O":
            print("You LOSE! The COMPUTER has WON !")
            exit()

    def check_If_Tie(board):
        if "-" not in board:
            print("It is a tie!")
            print("")
            print("Try again later!")
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

