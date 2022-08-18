from itertools import count
import random

lucky = 0


while lucky == 0:
    cnt = 0
    # user_guess = []
    user1 = int(input(" Enter your guess 1  :"))
    user2 = int(input(" Enter your guess 2  :"))
    user3 = int(input(" Enter your guess 3  :"))
    # user_guess.append(user1)
    # user_guess.append(user2)
    # user_guess.append(user3)

    lot_nums = []
    lot1 = random.randint(1, 9)
    lot2 = random.randint(1, 9)
    lot3 = random.randint(1, 9)

    lot_nums.append(lot1)
    lot_nums.append(lot2)
    lot_nums.append(lot3)

    for i in range(0, len(lot_nums)):
        if user1 == lot1 or user1 == lot2 or user1 == lot3:
            cnt += 1
