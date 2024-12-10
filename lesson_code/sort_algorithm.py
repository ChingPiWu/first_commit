import math_problem

def bubble_sort(nums:list):
    ##Bubble Sort
  sum= 0
  for j in range(len(nums)-1):
    for i in range(len(nums)-1):
      if nums[i]>nums[i+1]:
        nums[i],nums[i+1] = nums[i+1],nums[i]
      else:
        continue
    sum+=1
    print(sum,nums)

  return nums


def selection_sort(nums:list):
    ##Selection sort
  min_i =0
  n = len(nums)
  for j in range(n-1):
    min_i =j
    for i in range(j+1,n):
      if nums[i]<nums[min_i]:
        min_i = i

    nums[j],nums[min_i] = nums[min_i],nums[j]

    print(f'round = {j},min_i = {min_i},nums = {nums}')
  return nums

if __name__ == '__main__':
    print("ABC")
    nums = [9, 5, 1, 3, 7]
    print("Bubble sort:", bubble_sort(nums))
    print("Selection sort:", selection_sort(nums))
else:
  print('ABC: ', __name__)