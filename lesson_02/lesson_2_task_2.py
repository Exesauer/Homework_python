def is_year_leap(year):
    if year % 4 == 0:
        if year % 100 == 0:
            if year % 400 == 0:
                return "True"
            else:
                return "False"
        return "True"
    else:
        return "False"

try:
    year = int(input("Введите год: "))
    if 1 <= year <= 9999:
        print(f"год {year}: {is_year_leap(year)}")
    else:
        print("Пожалуйста, введите число в диапазоне от 1 до 9999.")
except ValueError:
    print("Пожалуйста, введите целое число от 1 до 9999.")