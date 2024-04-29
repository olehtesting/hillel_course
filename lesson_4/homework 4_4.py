# Створення порожнього списку
result = []

# Заповнення списку числами від 1 до 100, використовуючи умови для заміни чисел
for i in range(1, 101):
    if i % 3 == 0 and i % 5 == 0:
        result.append("FizzBuzz")
    elif i % 3 == 0:
        result.append("Fizz")
    elif i % 5 == 0:
        result.append("Buzz")
    else:
        result.append(i)

# Виведення результату
print(result)
