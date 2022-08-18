from random import randint

correct = 0
incorrect = 0

for i in range(10):
    no1 = randint(1, 12)
    no2 = randint(1, 12)
    real_Answer = no1*no2
    print("What is", str(no1), " X ", str(no2), "?: ")
    answer = int(input("What is the answer ?:  "))

    if answer == real_Answer:
        print("You are correct !")
        correct = correct + 1
    elif not answer == real_Answer:
        print("Incorrect, the answer is :", real_Answer)
        incorrect = incorrect + 1


print(f"""You are done !
You have {correct} correct and {incorrect} wrong """)
