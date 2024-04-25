def split_list(lst):
    if not lst:
        return [[], []]
    elif len(lst) % 2 == 0:
        split_index = len(lst) // 2
        return [lst[:split_index], lst[split_index:]]
    else:
        split_index = len(lst) // 2 + 1
        return [lst[:split_index], lst[split_index:]]


examples = [
    ([1, 2, 3, 4, 5], [[1, 2, 3], [4, 5]]),
    ([1, 2, 3, 4], [[1, 2], [3, 4]]),
    ([], [[], []])
]

#
for example, expected_output in examples:
    output = split_list(example)
    print(f"Було: {example} => Стало: {output} (Очікувано: {expected_output})")