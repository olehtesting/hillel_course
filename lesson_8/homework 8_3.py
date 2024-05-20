def find_unique_value(some_list):
    # Створити словник для підрахунку частоти кожного числа
    frequency = {}

    # Підрахунок частоти кожного числа в списку
    for number in some_list:
        if number in frequency:
            frequency[number] += 1
        else:
            frequency[number] = 1

    # Знайти та повернути число, яке зустрічається лише один раз