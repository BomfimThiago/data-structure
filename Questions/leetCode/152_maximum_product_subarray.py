"""
Given an integer array nums, find a 
subarray
 that has the largest product, and return the product.

The test cases are generated so that the answer will fit in a 32-bit integer.

Example 1:

Input: nums = [2,3,-2,4]
Output: 6
Explanation: [2,3] has the largest product 6.
Example 2:

Input: nums = [-2,0,-1]
Output: 0
Explanation: The result cannot be 2, because [-2,-1] is not a subarray.
"""
def maxProduct(nums):
    maxP = 0
    currMax, currMin = 1, 1

    if len(nums) == 1:
        return nums[0]

    for n in nums:
        if n == 0:
            currMax, currMin = 1, 1
            continue
        
        tmp =  max(n * currMax, n * currMin, n)
        currMin = min(n * currMax, n * currMin, n)
        currMax = tmp

        maxP = max(maxP, currMax)
    
    return maxP

if __name__ == "__main__":
    print(maxProduct([2,-5,-2,-4,3]))