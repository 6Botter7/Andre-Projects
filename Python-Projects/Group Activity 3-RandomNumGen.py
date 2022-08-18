# Imports the random funtion
import random
# Creates an empty list/Array assigned to a variable called even_num
even_num = []
# loop through this command 10 times.
for i in range(10):
    # Give me a random number between 10 and 50 and assign it to a new variable called random_num
    random_num = random.randint(10, 50)
    # If 2 can go into the random number without having a additional decimal value left then...//
    if (random_num % 2) == 0:
        # //...take that number and add it to the empty list/Array.
        even_num.append(random_num)
    # Print the random generated number in the console.
    print(random_num)

# Print this string with the updated even_num list after the loop is finished.
print(f"""Your even numbers are
    {even_num}""")
