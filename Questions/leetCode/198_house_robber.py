"""
You are a professional robber planning to rob houses along a street. Each house has a certain amount of money stashed, the only constraint stopping you from robbing each of them is that adjacent houses have security systems connected and it will automatically contact the police if two adjacent houses were broken into on the same night.

Given an integer array nums representing the amount of money of each house, return the maximum amount of money you can rob tonight without alerting the police.

Example 1:

Input: nums = [1,2,3,1]
Output: 4
Explanation: Rob house 1 (money = 1) and then rob house 3 (money = 3).
Total amount you can rob = 1 + 3 = 4.
Example 2:

Input: nums = [2,7,9,3,1]
Output: 12
Explanation: Rob house 1 (money = 2), rob house 3 (money = 9) and rob house 5 (money = 1).
Total amount you can rob = 2 + 9 + 1 = 12.

"""
from typing import List

# top down
def rob(nums):
    def dfs(i, cache):
        if i >= len(nums):
            return 0

        if i in cache:
            return cache[i]

        cache[i] = max(
            nums[i] + dfs(i + 2, cache),
            dfs(i + 1, cache)
        )

        return cache[i]

    return dfs(0, {})

# bottom up
def rob(nums: List[int]) -> int:
    current_max = 0 
    previous_max = 0

    for i in range(len(nums) - 1, -1, -1):
        tmp = current_max
        current_max = max(
            nums[i],
            nums[i] + previous_max,
            current_max
        )
        
        previous_max = tmp

    return current_max
   
        
if __name__ == "__main__":
    print(rob([2, 1, 1, 2]))
