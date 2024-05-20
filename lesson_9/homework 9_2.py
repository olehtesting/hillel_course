def difference(*args):
    # Якщо аргументів немає, повертаємо 0
    if not args:
        return 0

    # Знаходимо максимальне і мінімальне значення
    max_value = max(args)
    min_value = min(args)

    # Повертаємо різницю між максимальним і мінімальним значенням
    return round(max_value - min_value, 2)


# Приклади використання функції з тестами
assert difference(1, 2, 3) == 2, 'Test1'
assert difference(5, -5) == 10, 'Test2'
assert difference(10.2, -2.2, 0, 1.1, 0.5) == 12.4, 'Test3'
assert difference() == 0, 'Test4'
print('OK')