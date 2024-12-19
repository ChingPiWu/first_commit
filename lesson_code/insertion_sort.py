def insertion_sort(nums):
    answer = list()
    for new in nums:
        if answer:
            is_insert = False
            for i, num in enumerate(answer):
                if new < num:
                    is_insert = True
                    answer = answer[:i]+[new]+answer[i:]
                    break
            if not is_insert:
                answer = answer + [new]
        else:
            answer = [new]
    return answer


if __name__ == "__main__":
    nums = [40, 30, 50, 60, 20]
    print("insertion sorted list:", insertion_sort(nums))
