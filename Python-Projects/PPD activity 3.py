import random

randArray = []

for i in range(20):
    randomNo = random.randint(1, 20)
    randArray.append(randomNo)
    print(randomNo)


for i in range(len(randArray)):
    if randomNo <= randArray[i]:
        randArray[i] = randArray[i] + 10

    elif randomNo == randArray[i]:
        randArray[i] = randArray[i]*2

    elif randomNo >= randArray[i]:
        randArray[i] = randArray[i]**2


print(randArray)
