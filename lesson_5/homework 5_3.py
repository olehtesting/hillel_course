import string

def to_hashtag(user_input):

    words = user_input.split()

    hashtag = '#' + ''.join(word.capitalize() for word in words if word.isalnum())

    if len(hashtag) > 140:
        hashtag = hashtag[:137] + '...'

    return hashtag

user_input = input("Введіть рядок: ")

user_input_no_punct = ''.join(char for char in user_input if char not in string.punctuation)
print("Хештег:", to_hashtag(user_input_no_punct))