def format_time(seconds):

    days, seconds = divmod(seconds, 86400)
    hours, seconds = divmod(seconds, 3600)
    minutes, seconds = divmod(seconds, 60)

    formatted_time = ""
    if days > 0:
        formatted_time += f"{days} {'день' if days == 1 else 'дні'} "
    else:
        formatted_time += "0 днів "
    formatted_time += f"{hours:02d}:{minutes:02d}:{seconds:02d}"
    return formatted_time

while True:
    try:
        seconds = int(input("Введіть кількість секунд (більше або дорівнює 0 і менше ніж 8640000): "))
        if 0 <= seconds < 8640000:
            break
        else:
            print("Будь ласка, введіть число в діапазоні від 0 до 8640000.")
    except ValueError:
        print("Будь ласка, введіть ціле число.")

print("Час у читабельному вигляді:", format_time(seconds))