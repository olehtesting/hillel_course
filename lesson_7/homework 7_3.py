def second_index(text, some_str):
    # Знайдемо індекс першого входження шуканого рядка
    first_index = text.find(some_str)

    # Якщо перше входження не знайдено, повертаємо None
    if first_index == -1:
        return None

    # Знаходимо індекс другого входження шуканого рядка, починаючи з позиції після першого входження
    second_index = text.find(some_str, first_index + 1)

    # Якщо друге входження не знайдено, повертаємо None
    if second_index == -1:
        return None

    return second_index

# Перевірка
assert second_index("sims", "s") == 3, 'Test1'
assert second_index("find the river", "e") == 12, 'Test2'
assert second_index("hi", "h") is None, 'Test3'
assert second_index("Hello, hello", "lo") == 10, 'Test4'
print('ОК')