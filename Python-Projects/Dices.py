import random
d1_num = ['1', '2', '3', '4', '5', '6']
d2_num = ['1', '2', '3', '4', '5', '6']


def roll():
    return random.randint(0, 5)


def dice_result():
    d1_index = roll()
    d2_index = roll()
    d1 = d1_num[d1_index]
    d2 = d2_num[d2_index]
    print(d1)
    print(d2)


dice_result()


name = 'Hello, world how are you?'

tst = name[:8]

slc = name[::-3]
print(name)
print(slc)
print(tst)


x = "20"
y = 3
c = x*y
print(c)

for x in range(2, 30, 2):
    print(x)

for z in range(7):
    print(f"no {z}")

num = []

for w in range(8):
    num.append(w)
print(num)
print(len(num))


for i in range(1, 12, 1):
    z = random.randint(1, 12)
    print(z)
    a = random.randint(1, 12)
    print(a)
