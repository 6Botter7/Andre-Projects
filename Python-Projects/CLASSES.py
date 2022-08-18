from turtle import color
from unicodedata import name


class Man:
    species = "Homo Sapien"  # Class attribute

    def __init__(self, name, age, gender):   # Instance Attribute
        self.name = name
        self.age = age
        self.gender = gender
        pass
     # Instance method

    def description(self):
        return print(f"{self.name} is {self.age} years old and a {self.species}")

    def __str__(self):
        return (f"{self.name} is {self.age} years old and a {self.species}")

    # Another instance method
    def speak(self, phrase):
        return print(f"{self.name} says {phrase}")


man1 = Man("Andre Williams", 26, "Male")
man2 = Man("Tommy Malan", 30, "He-male")
man2.species = "Homo Neanderthal"

print(man1, man2)

# print(man1.name, man1.age, man1.gender, man1.species)
# # print(man2.species = "Homo Neanderthal")    #How to change variable Species?
# print(man2.name, man2.age, man2.gender, man2.species)

# -----------------------------------------------------
man1.speak("The KING is BACK !!")
man1.description()
man2.speak("I like turtles")
man2.description()
man1.__str__()

# print(man1.speak("The KING is BACK !!"))
# print(man1.description())
# -----------------------------------------------------------------------------------------------------------------------------------


class Car:
    color = "none"
    # mileage = str(mileage)

    def __init__(self, color, mileage):
        self.color = color
        self.mileage = mileage
        return print(f"The {color} car has {mileage} miles on the clock")

    def build_car(self, make, top_speed, engin):
        return print(f"My car is a {color} {make}, that has a top speed of {top_speed},with a {engin} engin")


car1 = Car("Blue", 20000)
car2 = Car("Red", 10000)


print(car1.color)
print(car2.mileage)

print("")
my_Car = Car("Black", 1000)
print(my_Car.color, my_Car.mileage)
print(my_Car.build_car("Ferrari", "300km/h", "3.0 L"))
# ----------------------------------------------------------------


class Bike:
    # color = input("Color of bike")                  #Is user input possible for class/objects
    # brand = input("Make of bike")

    def __init__(self, colour, make, size, speed):
        # self.make = input("Choose a color")
        self.colour = colour
        # self.colour = input("Choose a make")
        self.make = make
        self.size = size
        self.speed = speed
        return print(f"I have a {colour} {make},with a {size} size engin that can reach a speed of {speed} km's per hour")

    def announce(self):
        pass


my_bike1 = Bike("green", "Vuka", "500cc", 800)


class Rifle:
    damage = 100
    range = 1000
    mag = 5

    def __init__(self, caliber, **kwargs):
        self.caliber = caliber
        pass

    def shot(self, round, **kwargs):
        self.mag -= round
        current_mag = self.mag

        print(f"You have {current_mag} rounds left")
        # if self.mag == 0:
        #     self.reload(bullet)

    def reload(self, bullet, **kwargs):
        self.mag = + int(bullet)
        print(f"You have loaded {bullet} rounds.")
        new_mag = self.mag = + bullet
# create a variable where the current mag is updated.
        print(f"You now have {new_mag} rounds in your mag.")


r308 = Rifle(".308")

r308.shot(1)
print(r308.mag)
r308.shot(1)
r308.shot(1)
r308.shot(1)
r308.reload(3)


class Target:
    value_of_target = 100
    pass
# --------------------------------------------------------------------------

# Sort of Wokring...

# class Car:
#     name = input("What car do you drive  ?  ")
#     fuelConsumption = int(input("What is the fuel consumption  ?  ")),
#     tankCapacity = int(input("What is the tank capacity  ?  ")),

#     def __init__(self, name):
#         self.name = name
#         print(f"Your car is a {name}")

#     def add_data(self, fuelConsumption, tankCapacity):
#         self.fuelConsumption = fuelConsumption
#         self.tankCapacity = tankCapacity

#         # print(self.fuelConsumption)
#         # print(self.tankCapacity)
#         print(
#             f"The average fuel consumption of {self.name} is {tankCapacity/fuelConsumption} km/l")


# car1 = Car(name)
# car1.add_data(11, 100)
# print("")
# car2 = Car(name)
# car2.add_data(12, 90)
# ----------------------------------------------------------
class Car:  # WOKRING
    fuelConsumption = 0,
    tankCapacity = 0,
    name = ""

    def __init__(self, name):
        self.name = name
        print(f"Your car is a {self.name}")

    def add_data(self, fuelConsumption, tankCapacity):
        self.fuelConsumption = fuelConsumption
        if fuelConsumption < 8:
            self.fuelConsumption = 8
        elif fuelConsumption > 25:
            self.fuelConsumption = 25
        self.tankCapacity = tankCapacity
        if tankCapacity < 30:
            self.tankCapacity = 30
        elif tankCapacity > 80:
            self.tankCapacity = 80
        print(f"Fuel Consumption is : {self.fuelConsumption}")
        print(f"Tank Capacity is : {self.tankCapacity}")

    def calculate_fuel(self):
        print(
            f"The average fuel consumption of {self.name} is {self.tankCapacity/self.fuelConsumption} km/l")


car1 = Car("Ferarri")
car1.add_data(26, 68)
car1.calculate_fuel()
print("")
car2 = Car("Bugatti")
car2.add_data(6, 90)
car2.calculate_fuel()
