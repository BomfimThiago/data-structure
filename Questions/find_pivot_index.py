# Quesiton 1
"""
Given an array of integers nums, calculate the pivot index of this array.

The pivot index is the index where the sum of all the numbers strictly to the left of the index is equal to the sum of all the numbers strictly to the index's right.

If the index is on the left edge of the array, then the left sum is 0 because there are no elements to the left. This also applies to the right edge of the array.

Return the leftmost pivot index. If no such index exists, return -1.

"""

from typing import List

def recursion_f(index, nums):
    if index <= 0 or index >= len(nums) - 1:
        return -1

    left = nums[:index]
    right = nums[index + 1:]

    if sum(left) == sum(right):
        return index

    if sum(left) > sum(right):
        index -= 1
        return recursion_f(index, nums)
    else:
        index += 1
        return recursion_f(index, nums)

# time complexity O(n ^ 2)
def pivotIndex(nums: List[int]) -> int:
    # get the len of the list
    # get the middle index(if len(10) the middle will be 4)
    # divide the list in left half before the middle index
    # and right half after the middle_index
    # compare the sum of the halfs
    # if true return middle_index
    # if not see which half is bigger
    # if is left then the new index is index - 1
    # if is right then the new index is index + 1
    # re-start the cycle

    # constraint
    # if index + 1 or index - 1 is out of the bound return -1
    # there is no index that satisfy the conditions

    # if list of nums is empty return -1 

    # if the sum of the 
  

    if not nums:
        return -1

    index = len(nums) // 2
    return recursion_f(index, nums)

# time complexity O(n)
def pivotIndex2(nums: List[int]) -> int:
    total_sum = sum(nums)
    left_sum = 0

    for i in range(len(nums)):
        total_sum -= nums[i]  # Update total sum by subtracting the current element
        if left_sum == total_sum:
            return i
        left_sum += nums[i]  # Update the sum of the left subarray

    return -1

if __name__ == "__main__":
    print(pivotIndex())
    print(pivotIndex([1,2,3]))
    print(pivotIndex([2,1,-1]))

