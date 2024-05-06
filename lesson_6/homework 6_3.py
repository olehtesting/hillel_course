def multiply_digits(number):
    result = 1
    for digit in str(number):
        result *= int(digit)
    return result

# Зчитування числа від користувача
while True:
    try:
        user_input = int(input("Введіть ціле число: "))
        break
    except ValueError:
        print("Будь ласка, введіть ціле число.")

# Перемноження цифр числа
product = multiply_digits(user_input)

# Виведення результату та перевірка, чи більше чи дорівнює він 9
while product > 9:
    print("Проміжний добуток:", product)
    product = multiply_digits(product)

print("Кінцевий добуток:", product)