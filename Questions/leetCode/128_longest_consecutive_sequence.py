"""
Given an unsorted array of integers nums, return the length of the longest consecutive elements sequence.

You must write an algorithm that runs in O(n) time.

Example 1:

Input: nums = [100,4,200,1,3,2]
Output: 4
Explanation: The longest consecutive elements sequence is [1, 2, 3, 4]. Therefore its length is 4.
Example 2:

Input: nums = [0,3,7,2,5,8,4,6,0,1]
Output: 9
"""
from typing import List


def longestConsecutive(nums: List[int]) -> int:
        # [100, 4, 200, 1, 3, 2]
        s = set(nums) # {}
        length = 0
        visited = set()
        for n in nums:
            if n in visited:
                continue

            visited.add(n)
            i = n - 1 # for 4, i would be 3
            j = n + 1 # for 4, j would be 5
            size = 1

            while i in s:
                visited.add(i)
                i -= 1
                size += 1

            while j in s:
                visited.add(j)
                j += 1
                size += 1

            length = max(length, size)
        
        return length