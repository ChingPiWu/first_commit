from insertion_sort import insertion_sort
from merge_sort import merge


def tim_sort(nums):
    if len(nums) <= 32:
        return insertion_sort(nums)

    else:
        mid_index = len(nums)//2
        left_part = nums[:mid_index]
        right_part = nums[mid_index:]
        sorted_left_part = tim_sort(left_part)
        sorted_right_part = tim_sort(right_part)
        result_merge_sort = merge(sorted_left_part, sorted_right_part)
        return result_merge_sort


if __name__ == '__main__':
    import random
    import time
    nums = random.choices(range(10000, k=1024))
    result = tim_sort(nums)

    assert result == sorted(nums), print('Wrong answers')
    print('Succeed!!!')
