import re


def clean_html(input_filename, output_filename='cleaned.txt'):
    # Читаємо вміст вхідного файлу
    with open(input_filename, 'r', encoding='utf-8') as file:
        content = file.read()

    # Використовуємо регулярні вирази для видалення HTML-тегів
    clean_text = re.sub(r'<.*?>', '', content)

    # Записуємо очищений текст у вихідний файл
    with open(output_filename, 'w', encoding='utf-8') as file:
        file.write(clean_text)


# Виклик функції для очищення файлу draft.html і запису результату в cleaned.txt
clean_html('draft.html', 'cleaned.txt')