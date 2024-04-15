"""
Given an integer array nums, return all the triplets [nums[i], nums[j], nums[k]] such that i != j, i != k, and j != k, and nums[i] + nums[j] + nums[k] == 0.

Notice that the solution set must not contain duplicate triplets.

 

Example 1:

Input: nums = [-1,0,1,2,-1,-4]
Output: [[-1,-1,2],[-1,0,1]]
Explanation: 
nums[0] + nums[1] + nums[2] = (-1) + 0 + 1 = 0.
nums[1] + nums[2] + nums[4] = 0 + 1 + (-1) = 0.
nums[0] + nums[3] + nums[4] = (-1) + 2 + (-1) = 0.
The distinct triplets are [-1,0,1] and [-1,-1,2].
Notice that the order of the output and the order of the triplets does not matter.
Example 2:

Input: nums = [0,1,1]
Output: []
Explanation: The only possible triplet does not sum up to 0.
Example 3:

Input: nums = [0,0,0]
Output: [[0,0,0]]
Explanation: The only possible triplet sums up to 0.
"""
from typing import List


def threeSum(nums: List[int]) -> List[List[int]]:
    res = []
        # first we order the array
    nums.sort()

    # for each position we need to see if the other 2 positions sum = 0
    # if the sum is too high, we decrise the right pointer
    # if the sum is too low, we increase the left pointer
    # if the sum is 0, we increase l and decrease r and add the set in our results


    # [-1,0,1,2,-1,-4]
    # [-4, -1, -1, 0, 1, 2]
    for i in range(len(nums)):
        if i + 1 >= len(nums):
            break # it means that I'm in the last number of my array
        
        if i - 1 >= 0: # this position 
            if nums[i] == nums[i - 1]:
                continue

        l = i + 1
        r = len(nums) - 1

        while l < r:
            if nums[i] + nums[l] + nums[r] == 0:
                res.append([nums[i], nums[l], nums[r]])
                l += 1
                while nums[l] == nums[l - 1] and l < r:
                    l += 1
            elif nums[i] + nums[l] + nums[r] > 0:
                r -= 1
            else:
                l += 1

    return res

if __name__ == "__main__":
    print(threeSum([-1,0,1,2,-1,-4]))