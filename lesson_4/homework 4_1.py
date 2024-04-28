def move_zeros(nums):

    zero_count = nums.count(0)
    nums = [num for num in nums if num != 0]
    nums.extend([0] * zero_count)
    return nums


nums = [0, 1, 0, 3, 12, 15, 0, 7, 44]
print(move_zeros(nums))