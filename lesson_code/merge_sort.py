import math
left = [10, 30, 40, 70]
right = [20, 50, 60, 90]

result = []

while len(left) > 0 and len(right) > 0:
    if left[0] < right[0]:
        result.append(left.pop(0))
    else:
        result.append(right.pop(0))
if len(left) > 0:
    result += left
else:
    result += right
print(result)


def merge(a: list, b: list):
    result = []

    while len(a) > 0 and len(b) > 0:
        if a[0] < b[0]:
            result.append(a.pop(0))
        else:
            result.append(b.pop(0))
    if len(a) > 0:
        result += a
    else:
        result += b
    return (result)


def merge_sort(nums):
    if len(nums) == 1:
        return nums
    else:
        mid_index = len(nums)//2
        left_part = nums[:mid_index]
        right_part = nums[mid_index:]
        sorted_left_part = merge_sort(left_part)
        sorted_right_part = merge_sort(right_part)
        result_merge_sort = merge(sorted_left_part, sorted_right_part)
        print(f"Level = {int(math.log2(len(result_merge_sort)))
                         } completed:", result_merge_sort)
        return result_merge_sort


if __name__ == "__main__":
    nums = [30, 10, 40, 70, 50, 90, 60, 20]
    result = merge_sort(nums)
    print("Sorted list:", result)
