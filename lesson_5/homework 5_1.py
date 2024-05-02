import string
import keyword


def is_valid_variable_name(name):

    if name[0].isdigit():
        return False

    if any(char.isupper() for char in name):
        return False

    if any(char != '_' and (char.isspace() or char in string.punctuation) for char in name):
        return False

    if name in keyword.kwlist:
        return False

    if len(name) > 1 and all(char == '_' for char in name):
        return False

    if " " in name:
        return False

    return True

user_input = input("Введіть рядок: ")
print(is_valid_variable_name(user_input))