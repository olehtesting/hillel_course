def reverse_number(number):

    reversed_number = (number % 10) * 10000 + ((number // 10) % 10) * 1000 + ((number // 100) % 10) * 100 + ((number // 1000) % 10) * 10 + (number // 10000)
    return reversed_number


user_input = int(input("Введіть 5-ти значне ціле число: "))


if 10000 <= user_input <= 99999:

    reversed_result = reverse_number(user_input)
    print("Перевернуте число:", reversed_result)
else:
    print("Будь ласка, введіть 5-ти значне ціле число.")