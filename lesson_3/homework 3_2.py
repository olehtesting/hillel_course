def move_last_to_first(lst):

    if len(lst) <= 1:
        return lst


    last_element = lst.pop()
    lst.insert(0, last_element)
    return lst


def main():

    n = int(input("Введіть кількість елементів у списку: "))


    my_list = []


    for i in range(n):
        element = int(input("Введіть число: "))
        my_list.append(element)


    modified_list = move_last_to_first(my_list)


    print("Список після перенесення останнього елемента на початок:", modified_list)



main()