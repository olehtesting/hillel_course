def calculate():
    while True:

        expression = input("Введіть вираз: ")


        try:
            result = eval(expression)
            print("Результат:", result)
        except Exception as e:
            print("Помилка:", e)


        continue_calculation = input("Продовжити обчислення? (yes/no): ")
        if continue_calculation.lower() != 'yes' and continue_calculation.lower() != 'y':
            break


calculate()