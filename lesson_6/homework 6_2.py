def format_time(seconds):
    days, remainder = divmod(seconds, 86400)
    hours, remainder = divmod(remainder, 3600)
    minutes, seconds = divmod(remainder, 60)

    time_str = ""

    # Визначення кількості днів і формування відповідного рядка
    if days >= 1:
        if days % 10 == 1 and days % 100 != 11:
            time_str += f"{days} день "
        elif 2 <= days % 10 <= 4 and (days % 100 < 10 or days % 100 >= 20):
            time_str += f"{days} дні "
        else:
            time_str += f"{days} днів "
    else:
        time_str += "0 днів "

    # Додавання годин, хвилин і секунд з провідними нулями
    time_str += f"{hours:02d}:{minutes:02d}:{seconds:02d}"

    return time_str


# Зчитування кількості секунд від користувача
while True:
    try:
        seconds = int(input("Введіть кількість секунд (більше або дорівнює 0 і менше ніж 8640000): "))
        if 0 <= seconds < 8640000:
            break
        else:
            print("Будь ласка, введіть число в діапазоні від 0 до 8640000.")
    except ValueError:
        print("Будь ласка, введіть ціле число.")

# Форматування і виведення часу
print("Час у читабельному вигляді:", format_time(seconds))
