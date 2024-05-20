def add_one(digits):
    # Перетворити список цифр у число
    number = 0
    for digit in digits:
        number = number * 10 + digit

    # Додати 1 до числа
    number += 1

    # Перетворити число назад у список цифр
    result = [int(digit) for digit in str(number)]

    return result


# Приклад використання функції
digits = [1, 2, 3, 4]
print(add_one(digits))  # Виведе: [1, 2, 3, 5]