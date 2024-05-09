def common_elements():

    multiples_of_3 = [num for num in range(0, 101) if num % 3 == 0]


    multiples_of_5 = [num for num in range(0, 101) if num % 5 == 0]


    common_elements_set = set(multiples_of_3) & set(multiples_of_5)

    return common_elements_set

assert common_elements() == {0, 75, 45, 15, 90, 60, 30}
print('ОК')