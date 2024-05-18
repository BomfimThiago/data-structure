"""
Given an integer array nums of unique elements, return all possible 
subsets
 (the power set).

The solution set must not contain duplicate subsets. Return the solution in any order.

Example 1:

Input: nums = [1,2,3]
Output: [[],[1],[2],[1,2],[3],[1,3],[2,3],[1,2,3]]
Example 2:

Input: nums = [0]
Output: [[],[0]]

"""
def subsets(nums):
    if not nums:
        return []

    res = [] # base

    def backtrack(i, curr):
        if i >= len(nums):
            res.append(curr.copy())
            return

        curr.append(nums[i])
        backtrack(i + 1, curr)


        # not to include nums[i]
        curr.pop()
        backtrack(i + 1, curr)

    
    backtrack(0, [])
    return res

# time complexity 2n 

if __name__ == "__main__":
    print(subsets(nums = [1,2,3]))
        