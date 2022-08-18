import time
from time import sleep

counter = 1

print(counter)

while True:
    time.sleep(1)
    counter = counter + 1
    print(counter)
    if counter == 3:
        print("")
        sleep(2)
        print("GOOOOOOOOOOOO")
        sleep(2)
    # elif counter == 6:
        print("""CODE
_______________________________________________""")
        break

myList = ['ONE', 'TWO', 'THREE', 'GOOOOOOOOOOO']

for s in range(len(myList)):
    print(myList[s])
    sleep(1.5)

loading = "LOADING"

for i in range(len(loading)):
    print(loading[i])
    sleep(0.5)


print("Hacker voice..")
print("I'm in....")
