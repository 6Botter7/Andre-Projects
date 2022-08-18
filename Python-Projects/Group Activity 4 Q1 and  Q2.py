# Question 1 - # How can an infinite loop be created using a Python while loop?
# ---------------
# A loop becomes a infinite loop if a condition never becomes FALSE or TRUE. The loop has no possible way of stopping or executing.
# Example: An exit condition that’s never reached
# A condition that makes the loop start over and over again
# Change the loop variable to a new value inside the loop
# A loop without an exit condition
#  A loop that doesn’t change the loop variable’s value
# Mixing up the increment (+=) or decrement (-=) operators
# Wrong logical comparison in the loop’s condition
# The continue statement at the wrong place


# What potential problem might this cause?
# ------------------------------------------
# An infinite loop can crash your program or browser and freeze your computer.

# How could that issue be resolved?
# ---------------------------------------------------------------
# You could try and close/terminate the terminal if it allows you or close the program. Otherwise you will have to reboot your system.
# to avoid a infinate loop try:
# Never leave the terminating condition to be dependent on the user.
# Ensure you have at least one statement within the loop that changes the value of the comparison variable.

t_height = float(input(" Enter the height in CM's  :  "))
t_base = float(input("Enter the base lenght in CM's :  "))


def calculate(t_height, t_base):
    t_area = t_height * (t_base/2)
    print(f"The area of the triangle is {t_area} cm ²")


calculate(t_height, t_base)
