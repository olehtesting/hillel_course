def sum_of_even_indexed(nums):

    if not nums:
        return 0


    even_sum = sum(nums[i] for i in range(0, len(nums), 2))

    last_element = nums[-1]

    result = even_sum * last_element
    return result



nums = [1, 3, 6, 9, 15]
print(sum_of_even_indexed(nums))