def correct_sentence(text):

    if text[0].islower():
        text = text[0].upper() + text[1:]

    if not text.endswith('.'):
        text += '.'

    return text


# Перевірка
assert correct_sentence("hello world") == "Hello world.", 'Test1'
assert correct_sentence("python is awesome") == "Python is awesome.", 'Test2'
assert correct_sentence("end with dot.") == "End with dot.", 'Test3'
assert correct_sentence("already correct.") == "Already correct.", 'Test4'
print('ОК')