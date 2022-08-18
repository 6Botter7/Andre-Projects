# This function adds two numbers
def add(x, y):
    return x + y

# This function subtracts two numbers


def subtract(x, y):
    return x - y

# This function multiplies two numbers


def multiply(x, y):
    return x * y

# This function divides two numbers


def divide(x, y):
    return x / y


x = input("value 1")
y = input("value 2")
calculate = input("choose between add, subtract,divide or multiply")


def sum(x, y):
    print('{} / {} = '.format(x, y))
    print(x / y)


print(sum)  # Not Working
