import string
import keyword


def is_valid_variable_name(name):
    # Перевірка чи починається з цифри
    if name[0].isdigit():
        return False

    # Перевірка чи містить великі літери
    if any(char.isupper() for char in name):
        return False

    # Перевірка на наявність пробілів та знаків пунктуації
    if any(char in string.punctuation and char != '_' for char in name):
        return False

    # Перевірка на імена ключових слів
    if name in keyword.kwlist:
        return False

    return True


# Запит введення користувача
user_input = input("Введіть ім'я змінної: ")

# Виведення результату перевірки
print(is_valid_variable_name(user_input))