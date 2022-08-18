import datetime
word = "Andre"
search = input()
if search == "Andre":
    print(word)
elif search == "Andr" or search == "Anre" or search == "Adre":
    print(f"Did you mean {word} ?")
else:
    print("We did not find a word of that spelling, Please try again")
# ===========================================================================================


class MAN:
    def __init__(self, name):
        self.name = name

    def speak(self):
        print("Helllo World!")


man1 = MAN("Andre")
man1.speak()


class Person():
    def __init__(self, nm, yb):
        self.name = nm
        self.yearOfBirth = yb

    @property
    def yearOfBirth(self):
        return self.__yearOfBirth

    @yearOfBirth.setter
    def yearOfBirth(self, yb):
        currentYear = int(datetime.date.today().year)
        while(yb >= currentYear):
            yb = int(input("Please enter a year before " +
                     str(currentYear) + ": "))
            self.__yearOfBirth = yb

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, nm):
        self.__name = nm

    def calculateAge(self):
        currentYear = datetime.date.today().year
        return "In " + str(currentYear) + ", " + str(self.name) \
            + " should be " + str(currentYear - self.yearOfBirth) \
            + " years of age."

    def __gt__(self, otherObject):
        ...

    # Create three Person objects, passing in their names and year of birth
person1 = Person("Joseph", 2001)
person2 = Person("Munati", 2008)
person3 = Person("Craig", 2005)

# Compare their ages
if (person1 > person2):
    print(person1.name + " is " + str(person1 > person2) +
          " years older than " + person2.name)
else:
    print(person1.name + " is not older than " + person2.name)

if (person2 > person3):
    print(person2.name + " is " + str(person2 > person3) +
          " years older than " + person3.name)
else:
    print(person2.name + " is not older than " + person3.name)

# Expected Output:
# Joseph is 7 years older than Munati
# Munati is not older than Craig

# What will happen if the following code is executed? (Assume the computer's OS date is set to 2020/6/6):
person4 = Person("Maria", 2025)


class Person():
    def __init__(self, nm, yb):
        self.name = nm
        self.yearOfBirth = yb

    @property
    def yearOfBirth(self):
        return self.__yearOfBirth

    @yearOfBirth.setter
    def yearOfBirth(self, yb):
        currentYear = int(datetime.date.today().year)
        while(yb >= currentYear):
            yb = int(input("Please enter a year before " +
                     str(currentYear) + ": "))
            self.__yearOfBirth = yb

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, nm):
        self.__name = nm

    def calculateAge(self):
        currentYear = datetime.date.today().year
        return "In " + str(currentYear) + ", " + str(self.name) \
            + " should be " + str(currentYear - self.yearOfBirth) \
            + " years of age."

    def __gt__(self, otherObject):
        ...

    # Create three Person objects, passing in their names and year of birth
person1 = Person("Joseph", 2001)
person2 = Person("Munati", 2008)
person3 = Person("Craig", 2005)

# Compare their ages
if (person1 > person2):
    print(person1.name + " is " + str(person1 > person2) +
          " years older than " + person2.name)
else:
    print(person1.name + " is not older than " + person2.name)

if (person2 > person3):
    print(person2.name + " is " + str(person2 > person3) +
          " years older than " + person3.name)
else:
    print(person2.name + " is not older than " + person3.name)

# Expected Output:
# Joseph is 7 years older than Munati
# Munati is not older than Craig

# What will happen if the following code is executed? (Assume the computer's OS date is set to 2020/6/6):
person4 = Person("Maria", 2025)


while True:
                if play_again == "y":
                    break

                else:
                    print("You chose to leave the game. GOODBYE !")
                    exit()