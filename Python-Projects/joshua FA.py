from cmath import nan
import random
guess_times = 0
guessed_numbers = []
print('this is a game, guess 3 numbers between 0 and 9')
while guess_times < 3:
    num1 = str(input('enter a number '))
    guessed_numbers.append(num1)
    guess_times += 1
print('you guessed ', guessed_numbers)


generated = []

while len(generated) < 3:
    random_num = str(random.randint(1, 10))
    generated.append(random_num)


print('the supposed are ', generated)


# for no in guessed_numbers:
#     if num1 in generated:
#         correct_guess.append(num1)
correct_guess = []


def checkWin(guessed_numbers, generated):
    num_correct = 0
    for i in range(0, len(generated)):
        value = generated[i]
        if value in guessed_numbers:
            num_correct += 1
            while value in guessed_numbers:
                guessed_numbers.remove(value)

    return num_correct

# for i in range(0, len(generated)):
#     count = 0
#     value = generated[i]
#     if value in guessed_numbers:
#         # while value in guessed_numbers:
#         # num_correct += 1
#         correct_guess.append(value)
#         count += 1
#         num_correct += 1
#         generated.remove(value)
#     else:
#         continue


    # generated.remove(value)
    # guessed_numbers.remove(value)
checkWin(guessed_numbers, generated)

print('your correct guesses  are', correct_guess)


# num_correct = len(correct_guess)
if num_correct == 1:
    print("You guessed 1 number correctly")
    print("Your reward: 10")
if num_correct == 2:
    print("You guessed 2 numbers correctly")
    print("Your reward: 100")
if num_correct == 3:
    print("You guessed 3 numbers correctly")
    print("Your reward: 1000")
if correct_guess == generated:
    print("You guessed all numbers in order")
    print("Your reward: 1,000,000")
if num_correct == 0:
    print("No matches")
    print("Your reward: 0")
