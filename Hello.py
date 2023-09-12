def check_even(number):
    if number % 2 == 0:
        return True
    else:
        return False

number = int(user_input)

if check_even(number):
    print("Число", number, "является четным.")
else:
    print("Число", number, "является нечетным.")