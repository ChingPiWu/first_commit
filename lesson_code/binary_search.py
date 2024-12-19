
import random
nums = random.choices(range(100), k=10)
nums = sorted(nums)
print(nums)


def binary_serch(nums):
    target = random.choice(nums)
    start = 0
    end = len(nums)-1

    while start <= end:
        mid = (start + end)//2
        mid_value = nums[mid]
        if mid_value < target:
            start = mid + 1
        elif mid_value > target:
            end = mid - 1
        else:
            return ("Find target at ", mid)
    return ("Not Found")
