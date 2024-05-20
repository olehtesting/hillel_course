def is_palindrome(text):
    # Видалити всі непотрібні символи та привести рядок до нижнього регістру
    cleaned_text = ''.join(char.lower() for char in text if char.isalnum())

    # Перевірити, чи є очищений рядок паліндромом
    return cleaned_text == cleaned_text[::-1]


# Приклад використання функції з тестами
assert is_palindrome('A man, a plan, a canal: Panama') == True, 'Test1'
assert is_palindrome('0P') == False, 'Test2'
assert is_palindrome('a.') == True, 'Test3'
assert is_palindrome('aurora') == False, 'Test4'
print("ОК")