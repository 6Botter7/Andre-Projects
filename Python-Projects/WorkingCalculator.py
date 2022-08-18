number_1 = float(input('Enter your first number: '))

operation = input('''
Please type in the math operation you would like to complete:
+ for addition
- for subtraction
* for multiplication
/ for division
''')

number_2 = float(input('Enter your second number: '))





if operation == '+':                               #add
    print('{} + {} = '.format(number_1, number_2))
    print(number_1 + number_2)

elif operation == '-':                             #subtract
    print('{} - {} = '.format(number_1, number_2))
    print(number_1 - number_2)

elif operation == '*':                             #multiply
    print('{} * {} = '.format(number_1, number_2))
    print(number_1 * number_2)

elif operation == '/':                             #divide
    print('{} / {} = '.format(number_1, number_2))
    print(number_1 / number_2)

else:
    print('You have not typed a valid operator, please run the program again.')