"""
Suppose an array of length n sorted in ascending order is rotated between 1 and n times. For example, the array nums = [0,1,2,4,5,6,7] might become:

[4,5,6,7,0,1,2] if it was rotated 4 times.
[0,1,2,4,5,6,7] if it was rotated 7 times.
Notice that rotating an array [a[0], a[1], a[2], ..., a[n-1]] 1 time results in the array [a[n-1], a[0], a[1], a[2], ..., a[n-2]].

Given the sorted rotated array nums of unique elements, return the minimum element of this array.

You must write an algorithm that runs in O(log n) time.

Example 1:

Input: nums = [3,4,5,1,2]
Output: 1
Explanation: The original array was [1,2,3,4,5] rotated 3 times.
Example 2:

Input: nums = [4,5,6,7,0,1,2]
Output: 0
Explanation: The original array was [0,1,2,4,5,6,7] and it was rotated 4 times.
Example 3:

Input: nums = [11,13,15,17]
Output: 11
Explanation: The original array was [11,13,15,17] and it was rotated 4 times. 
 
"""
from typing import List

from typing import List

def findMin(nums: List[int]) -> int:
    m = len(nums) // 2
    l = 0
    r = len(nums) - 1
    left = nums[l: m]
    right = nums[m+1:r]
    
    def getMin(left, right):
        if len(left) > 1:
            m = len(left) // 2
            l = left[0: m]
            r = left[m:len(left)]
            getMin(l, r)

        if len(right) > 1:
            m = len(right) // 2
            l = right[0: m]
            r = right[m:len(right)]
            getMin(l, r)

        return left[0] if left[0] <= right[0] else right[0]

    res = getMin(left, right)
    
    return res


if __name__ == "__main__":
    print(findMin([4,5,6,1,2,3]))