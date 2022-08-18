prompt = input("Binary or Decimal. Enter (b/d)  ?")

if prompt == "b":
    numberB = int(input("Enter your number here"))
    binNum = bin(numberB)
    print(numberB)

elif prompt == "d":
    numberD = int(input("Enter your number here"))
    decNum =

    c = input(
        "Do you want a binary number or decimal number converted  : ").lower()[0]
if c == "b":
    num = int(input("enter the number you want converted: "))
    b = bin(num) 
    print(b)
elif c == "d":
    num = input("enter the number you want converted: ") 
    d = int(num, 2) 
    print(d)
else:
    print("invalid option")

# ---------------------------------------------------------
