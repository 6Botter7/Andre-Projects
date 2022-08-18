from tkinter import Menu
from unicodedata import name


class Animal:
    def __init__(self, animalName):
        self.animalName = animalName

    def whatIsOnTheMenu(self, menu):
        self.menu = menu
        print(f"Today's menu is{self.menu}")


class Dog(Animal):
    def __init__(self, todayFood, name):
        self.todayFood = todayFood
        self.name = name
        self.species = super().__init__(animalName="...")
        # -------------------------------================-----> tried Animal  too

    def todaysMenu(self):
        super().whatIsOnTheMenu()

        print(super().whatIsOnTheMenu)


dog1 = Dog(Animal("Homo Sapien"), ("Malan"))
dog2 = Animal("Hond")
dog3 = Dog(Animal("Canine"), "Doggy")

# dog1.todaysMenu()
dog1.name
dog1.whatIsOnTheMenu("Pizza")
# print(dog1.animalName)
dog2.whatIsOnTheMenu("Burgers")
print(dog2.animalName)
print(dog1.name)

print(
    f"The species of dog 3 are {dog3.species} and we call him {dog3.name}")
# -----------------------------==============------------------------------> tried {dog3.animalName}  too


# print(dog1.name("Name"))


class Rectangle():
    def __init__(self, length, width):
        self.length = length
        self.width = width

    def display_area(self):
        area = self.length*self.width
        print(area)


rect1 = Rectangle(10, 20)
rect1.display_area()
