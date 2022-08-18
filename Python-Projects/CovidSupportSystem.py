from tkinter import Y
x = 0
while x == 0:

    print("Welcome to the COVID-19 support service. Please select an option below:  ")
    print("1. Statistics")
    print("2. Prevention")
    print("3. Symptoms")
    print("4. Treatment")
    print("5. Report case")
    print("6. Exit")
    choice = input("Enter choice (1/2/3/4/5/6): ")
    user_input = choice
    user_choice = ["1", "2", "3", "4", "5", "6"]
    countries = [("Germany currently has 14562 Confirmed cases"),
                 ("Italy currently has 212245 Confirmed cases"),
                 ("New Zeeland currently has 400 Confirmed cases"),
                 ("Canada currently has 4223 Confirmed cases"),
                 ("Brazil currently has 69874 Confirmed cases"),
                 ("Argentina currently has 78945 Confirmed cases"),
                 ("Spain currently has 9664 Confirmed cases"),
                 ("Finland currently has 124 Confirmed cases"),
                 ("Vietnam currently has 17895 Confirmed cases"),
                 ("Russia currently has 829 Confirmed cases")]

    if choice == "1":
        print("Currently in SA there are 27403 confirmed cases")
        print("Currently in USA there are 170000 Confirmed cases")
        print("Currently in China there are 82995 Confirmed cases")
        selectOpt = input(
            "Would you like to see the Confirmed casses for a random country? y/n : ")

        while selectOpt == "y":
            if selectOpt == "y":
                country_No = input(
                    "To select a  random country, type a number from 0 to 9, Type 'e' to exit: ")
                if country_No == "0":
                    print(countries[0])

                elif country_No == "1":
                    print(countries[1])
                    # selectOpt = input(
                    #     "Would you like to see the Confirmed casses for a random country? y/n : ")
                elif country_No == "2":
                    print(countries[2])
                elif country_No == "3":
                    print(countries[3])
                elif country_No == "4":
                    print(countries[4])
                elif country_No == "5":
                    print(countries[5])
                elif country_No == "6":
                    print(countries[6])
                elif country_No == "7":
                    print(countries[7])
                elif country_No == "8":
                    print(countries[8])
                elif country_No == "9":
                    print(countries[9])
                elif country_No == "e":
                    break

    if choice == "2":
        print("""To prevent the spread of COVID-19: 
    Clean your hands often. 
    Use soap and water, or an alcohol—based hand rub.Maintain a safe distance from anyone who is coughing or sneezing. 
    Don’t touch your eyes, nose or mouth. 
    Cover your nose and mouth with your bent elbow or a tissue when you cough or sneeze. 
    Stay home if you feel unwell. 
    If you have a fever, cough and difficulty breathing, seek medical attention. Call in advance.
    Follow the directions of your local health authority.""")

    if choice == "3":
        print("""Most common symptoms:
    fever
    dry cough
    tiredness

    Less common symptoms:
    aches and pains
    sore throat
    diarrhoea
    conjunctivitis
    headache
    loss of taste or smell
    a rash on skin, or discolouration of fingers or toes

    Serious symptoms:
    difficulty breathing or shortness of breath
    chest pain or pressure
    loss of speech or movement.  """)

    if choice == "4":
        print("""If you feel sick you should rest, drink plenty of fluid, and eat nutritious food. Stay in a separate room
    from other family members, and use a dedicated bathroom if possible. Clean and disinfect
    frequently touched surfaces.  """)

    while choice == "5":
        if choice == "5":
            symptom = input("Do you have any of the symptoms? y/n: ")
            temp = input("Is your temperature above 38.5°C ? y/n:  ")
            your_country = print("""In which Country are you ? Please select an option below:  
            1. South Africa
            2. USA
            3. China""")
            input("Enter Option (1/2/3): ")

        if symptom == "y":
            print("You have Covid-19, please seek medical attention!")
            break
        elif temp == "y":
            print("You have Covid-19, stay safe!")
            break
        else:
            if symptom == "n" and temp == "n":
                print("You do not have Covid-19 !")
                break

    if choice == "6":
        print("Goodbye")
        x += 1
