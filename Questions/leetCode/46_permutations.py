"""
Given an array nums of distinct integers, return all the possible permutations. 
You can return the answer in any order.

 

Example 1:

Input: nums = [1,2,3]
Output: [[1,2,3],[1,3,2],[2,1,3],[2,3,1],[3,1,2],[3,2,1]]
Example 2:

Input: nums = [0,1]
Output: [[0,1],[1,0]]
Example 3:

Input: nums = [1]
Output: [[1]]

"""
def permute(nums):
    res = []
    def dfs(i, curr, cache):
        print("curr", curr)
        if len(curr) == len(nums):
            res.append(curr.copy())
            return

        curr.append(nums[i])
        n = len(nums) - 1
        while n:
            j = i
            n = n - j
            j += 1
            dfs(n, curr, cache)

    # for i in range(len(nums)):
        
    dfs(0, [], set())

    return res

if __name__ == "__main__":
    nums = [1,2,3]
    nums2 = [0, 1]
    print(permute(nums))