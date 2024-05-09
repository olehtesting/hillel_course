def common_elements():
    # Генеруємо перший список чисел кратних 3
    multiples_of_3 = [num for num in range(0, 101) if num % 3 == 0]

    # Генеруємо другий список чисел кратних 5
    multiples_of_5 = [num for num in range(0, 101) if num % 5 == 0]

    # Створюємо множину з числами, які є в обох списках (перетин)
    common_elements_set = set(multiples_of_3) & set(multiples_of_5)

    return common_elements_set

# Перевірка
assert common_elements() == {0, 75, 45, 15, 90, 60, 30}
print('ОК')