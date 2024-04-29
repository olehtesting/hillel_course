import random

random_list = random.sample(range(100), random.randint(3, 10))
print("Початковий список:", random_list)

new_list = [random_list[0], random_list[-3], random_list[-2]]
print("Новий список:", new_list)