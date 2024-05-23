def first_word(text: str) -> str:
    """Знаходить перше слово у рядку"""
    # Видаляємо всі символи крім літер та апострофа
    clean_text = ''.join(char if char.isalpha() or char == "'" else ' ' for char in text)
    # Розділяємо рядок на слова за пробілами
    words = clean_text.split()
    # Повертаємо перше слово
    return words[0]

if __name__ == "__main__":
    # Тести
    assert first_word("Hello world") == "Hello", 'Test1'
    assert first_word("greetings, friends") == "greetings", 'Test2'
    assert first_word("don't touch it") == "don't", 'Test3'
    assert first_word(".., and so on ...") == "and", 'Test4'
    assert first_word("hi") == "hi", 'Test5'
    assert first_word("Hello.World") == "Hello", 'Test6'
    print('OK')