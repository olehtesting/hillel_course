import string

def characters_between(letters):
    start, end = letters.split('-')
    start_index = string.ascii_letters.index(start)
    end_index = string.ascii_letters.index(end)
    return string.ascii_letters[start_index:end_index+1]

letters = input("Введіть дві літери через дефіс (наприклад, a-b): ")
print("Символи між введеними літерами:", characters_between(letters))