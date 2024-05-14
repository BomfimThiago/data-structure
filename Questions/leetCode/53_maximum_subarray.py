"""
53. Maximum Subarray
Medium
Topics
Companies
Given an integer array nums, find the 
subarray
 with the largest sum, and return its sum.

Example 1:

Input: nums = [-2,1,-3,4,-1,2,1,-5,4]
Output: 6
Explanation: The subarray [4,-1,2,1] has the largest sum 6.
Example 2:

Input: nums = [1]
Output: 1
Explanation: The subarray [1] has the largest sum 1.
Example 3:

Input: nums = [5,4,-1,7,8]
Output: 23
Explanation: The subarray [5,4,-1,7,8] has the largest sum 23.

"""
def maxSubArray(nums):
    # subarray contiguous non empty array
    maxS = nums[0]
    currS = 0
    for n in nums:
        if currS < 0:
            currS = 0
        currS += n
        maxS = max(currS, maxS)

    return maxS

if __name__ == "__main__":
    print(maxSubArray(nums = [-2,1,-3,4,-1,2,1,-5,4]))