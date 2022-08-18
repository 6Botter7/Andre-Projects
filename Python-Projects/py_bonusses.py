bonus_chart = [
    [5.00, 9.00, 16.00, 22.00, 30.00],
    [10.00, 12.00, 18.00, 24.00, 36.00],
    [20.00, 25.00, 32.00, 42.00, 53.00],
    [32.00, 38.00, 45.00, 55.00, 68.00],
    [46.00, 54.00, 65.00, 77.00, 90.00],
    [60.00, 72.00, 84.00, 96.00, 120.00],
    [85.00, 100.00, 120.00, 140.00, 175.00]
]

con = 0
while con == 0:

    no_weeks = int(input("Enter number of weeks worked  (max = 6): "))
    while no_weeks > 6 and no_weeks <= 998:
        print("The max is 6, try again")
        no_weeks = int(input("Enter number of weeks worked  (max = 6): "))
    if no_weeks == 999:
        con += 1
        print("Goodbye...")
        break

    no_pos_reviews = int(
        input("Enter number of Positive reviews received (max = 4) : "))

    while no_pos_reviews > 4 and no_pos_reviews < 998:
        print("The max is 4, try again")
        no_pos_reviews = int(
            input("Enter number of Positive reviews received (max = 4) : "))
    if no_pos_reviews == 999:
        con += 1
        print('Goodbye')
        break

    bonus = bonus_chart[no_weeks][no_pos_reviews]

    print(f"${bonus} received")
