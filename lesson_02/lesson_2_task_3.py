import math

def square(side):
    area = side * side
    return area

while True:
    try:
        user_input = float(input("Введите сторону квадрата: "))
        if user_input < 0:
            print("Ошибка: Сторона не может быть отрицательной. Повторите ввод")
        else:
            break  # Выход из цикла, если введено корректное значение
    except ValueError:
        print("Ошибка: Доступен ввод только чисел. Повторите ввод")

# Округление стороны
rounded_side = math.ceil(user_input)
# Вычисление площади
output = square(rounded_side)
# Вывод результата
print("Площадь квадрата:", output)
