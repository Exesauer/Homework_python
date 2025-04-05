def month_to_season(month):
    if month < 1 or month > 12:
        print("Некорректный месяц")
    else:
        if month == 12 or month == 1 or month == 2:
            print("Зима")
        elif month == 3 or month == 4 or month == 5:
            print("Весна")
        elif month == 6 or month == 7 or month == 8:
            print("Лето")
        elif month == 9 or month == 10 or month == 11:
            print("Осень")

month = int(input("Введите месяц: "))

month_to_season(month)