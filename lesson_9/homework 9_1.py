def popular_words(text, words):
    # Перевести весь текст в нижній регістр
    text = text.lower()

    # Розбити текст на слова
    word_list = text.split()

    # Створити словник для зберігання результатів
    word_count = {}

    # Ініціалізувати словник нулями для кожного шуканого слова
    for word in words:
        word_count[word] = 0

    # Порахувати кількість появ кожного шуканого слова в тексті
    for word in word_list:
        if word in word_count:
            word_count[word] += 1

    return word_count


# Приклад використання функції з тестами
assert popular_words('''When I was One I had just begun When I was Two I was nearly new ''',
                     ['i', 'was', 'three', 'near']) == {'i': 4, 'was': 3, 'three': 0, 'near': 0}, 'Test1'
print('OK')