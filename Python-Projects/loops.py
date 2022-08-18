attempts = 0  # Creates a Variable and gives a value of 0
# Creates a while loop and says : While the value of attempts(above declared variable), is less than 3, continue the loop
while attempts < 3:
    # While the loop is running and attempts are still less tan 3, create a new variable called "number", and number is equal to the input of the user (int(input("some string")))
    number = int(input("Enter a number"))
    # Create another new variable, called numberSquare, and that variable is equal to the user's input squared(**2)
    numberSquare = number**2
    # After this is done, update the attempt value by adding 1, So attempts will now be 1(attempts = 1). This will run over and over umtil attempts(the variable), is equal to 3
    attempts = attempts + 1
    # Then we print the value of numberSquare (User input **2)
    print(numberSquare)
# -------------------------------------------------------------------------------------------------
# note the indentation, all the above is in the while loop, the while loop runs until attempts are less than 3, then stops.
# the Print is a new funtion we call, outside the loop, so when the loop is done, please print this (In this case it is the words in the string"")
print("the loop is done!")


# prompt the user 3 times, after 3 times break loop and print
# ------------------------------------------------------------
tries = 0  # We create a variable called "tries", with a value of 0

# We start our for loop. We basically say 'i' is equal to 3 times, so the loop will run for 3 times.
for i in range(3):
    # in the for loop, create a new variable called "nom", and nom is equal to the input pf the user (input funtion)
    nom = int(input("enter a nimber to be squared"))
    # we create another variable, "nomS", and this variable is equal to the user's input squared(**2)
    nomS = nom**2
    print(nomS)  # please print the value of nomS
    # After the print please update the variable called "tries" (above, in the beginning),by adding 1
    tries = tries + 1
    if tries == 3:  # then we write an If statement inside the For loop. The statement says : If the variable called "tries", is equal to 3, then...:
        # Print the value of the variable called tries, dont worry about the 'f' infront of the string or the {}curly brackets, we will cover that later. You can just say: print(tries)
        print(f"Your total tries were {tries}")
        print("Your loop is done")  # Print the string("") "Your loop is done"5
