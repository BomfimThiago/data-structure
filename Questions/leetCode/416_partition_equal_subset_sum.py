"""
Given an integer array nums, return true if you can partition the array 
into two subsets such that the sum of the elements in both subsets is equal or false otherwise.

Example 1:

Input: nums = [1,5,11,5]
Output: true
Explanation: The array can be partitioned as [1, 5, 5] and [11].
Example 2:

Input: nums = [1,2,3,5]
Output: false
Explanation: The array cannot be partitioned into equal sum subsets.
"""
def can_partition(nums):
    sum_set = set()
    res = []
    def dfs(i, curr, total):
        cache = set()
        sum = 0

        if i in cache:
            return 0
        
        print(i)
        if i == len(nums):
            res.append(curr.copy())
            print(total)
            return 0

        curr.append(nums[i])
        dfs(i + 1, curr, total + nums[i])
        curr.pop()
        dfs(i + 1, curr, total)
    dfs(0, [], 0)
    return res

if __name__ == "__main__":
    print(can_partition([1, 5, 11, 5]))