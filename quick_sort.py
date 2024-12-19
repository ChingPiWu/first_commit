def quick_sort(nums):
    if len(nums) <= 1:
        return nums
    else:
        pivot = nums[0]
        left_part = list()
        right_part = list()
        for num in nums[1:]:
            if num < pivot:
                left_part.append(num)
            else:
                right_part.append(num)
        print(f'{left_part} [{pivot}] {right_part}')
        return quick_sort(left_part) + [pivot] + quick_sort(right_part)


if __name__ == '__main__':
    nums = [50, 90, 70, 20, 10, 30, 40, 60, 80]
    quick_sort(nums)
