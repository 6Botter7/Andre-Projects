import requests
import json
run = True
while run == True:
    user_input = str(input("Welcome to the AA calculator.\n Please select one of the following options : \n 1. Have a look at the previous entry. \n 2. Make a new entry. \n 3. Close the Program  \n Entry  :  "))

    if user_input == "2":
        meters = float(input("How many meters have you traveled ? "))
        kilometers = meters/1000
        print(kilometers)

        car_select = input(
            "Please select one of the following : \n 1. Hatchback  \n 2. SUV   \n3. Sportscar  \n Entry  :  ")
        AA_calc = "https://raw.githubusercontent.com/tyrone0501/AA-Petrol-Price/main/Cars.json"
        response = requests.get(AA_calc)
        response_json = response.json()

        if car_select == "1":
            siteresponse = response_json["Hatchback"]*kilometers
            print(siteresponse)
        elif car_select == "2":
            siteresponse = response_json["SUV"]*kilometers
            print(siteresponse)
        elif car_select == "3":
            siteresponse = response_json["Sportscar"]*kilometers
            print(siteresponse)
        else:
            print("Please enter a valid number.")

        reason = input(
            "Enter your description on where you traveled and why  :  ")

        data = {
            'Cost': siteresponse,
            'KMs': kilometers,
            'Description': reason
        }
        dict_1 = json.dumps(data)  # converting dictionary to JSON

    elif user_input == "1":
        print(
            f"Here is the previous entry  :  \n Yourn amount of kilometers are  :{kilometers}.\n Your total cost is {siteresponse}. \n Your Description {reason}")
        print("")
        print(dict_1)

    elif user_input == "3":
        print("Goodbye...")
        run = False

    else:
        print("Enter a valid response !!!  ")
