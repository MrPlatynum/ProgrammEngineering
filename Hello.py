def check_even(number):
    if number % 2 == 0:
        return True
    else:
        return False

# Получение числа от пользователя
number = int(user_input)

# Проверка четности числа и вывод результата
if check_even(number):
    print("Число", number, "является четным.")
else:
    print("Число", number, "является нечетным.")