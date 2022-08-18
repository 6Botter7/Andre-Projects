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
