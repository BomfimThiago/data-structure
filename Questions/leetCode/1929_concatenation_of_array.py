"""
Given an integer array nums of length n, you want to create an array ans of length 2n where ans[i] == nums[i] and ans[i + n] == nums[i] for 0 <= i < n (0-indexed).

Specifically, ans is the concatenation of two nums arrays.

Return the array ans.

 

Example 1:

Input: nums = [1,2,1]
Output: [1,2,1,1,2,1]
Explanation: The array ans is formed as follows:
- ans = [nums[0],nums[1],nums[2],nums[0],nums[1],nums[2]]
- ans = [1,2,1,1,2,1]
Example 2:

Input: nums = [1,3,2,1]
Output: [1,3,2,1,1,3,2,1]
Explanation: The array ans is formed as follows:
- ans = [nums[0],nums[1],nums[2],nums[3],nums[0],nums[1],nums[2],nums[3]]
- ans = [1,3,2,1,1,3,2,1]
"""
from typing import List

# this solution works for just for when we want to duplicate the original array
def getConcatenation(nums: List[int]) -> List[int]:
    size = len(nums)
    ans = [0 for _ in range(2 * size)]

    # 1 2 1 
    for i in range(size):
        ans[i] = nums[i]
        ans[i + size] = nums[i]
    
    return ans

# this solution is for when we want to make the number to multiply the original array dynamic
# k could be any number
def getConcatenation(nums: List[int]) -> List[int]:
    ans = []
    k = 2

    for i in range(k):
        for n in nums:
            ans.append(n)
    return ans