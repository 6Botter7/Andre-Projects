drink_options=["beer","wyn","brannewyn","whiskey","gin","vodka","koeldrank"]
shoot_options=["Jaggy","Tequila","Sour","Geen","ToffieAppel", "Stroh Rum", "Bombs"]

import random

def choice():
    return random.randint(0, 6)

def drink_of_the_night():
    drink_index = choice()
    shoot_index = choice()
    drink = drink_options[drink_index]
    shooter = shoot_options[shoot_index]
    print("Jou drink is :  ", drink)
    print("Jou shooter is:  ", shooter)    

drink_of_the_night()    