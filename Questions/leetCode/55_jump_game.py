"""
You are given an integer array nums. You are initially positioned at the array's first index, 
and each element in the array represents your maximum jump length at that position.

Return true if you can reach the last index, or false otherwise.

Example 1:

Input: nums = [2,3,1,1,4]
Output: true
Explanation: Jump 1 step from index 0 to 1, then 3 steps to the last index.
Example 2:

Input: nums = [3,2,1,0,4]
Output: false
Explanation: You will always arrive at index 3 no matter what. Its maximum jump length is 0, which makes it impossible to reach the last index.

"""
# this has complexity O(n2)
def canJump(nums):
    if len(nums) == 1:
        return True

    # trying dynamic approach
    n = len(nums)
    dp = [False] * n
    dp[n - 1] = True
    n_steps = 1
    for i in range(n - 2, -1, -1):
        if nums[i] == 0:
            dp[i] = False
        elif nums[i] >= n_steps:
            dp[i] = True
        else:
            dp[i] = any([reached for reached in dp[i + 1: i + nums[i] + 1]])

        n_steps += 1

    return dp[0]

def canJump2(nums):
    last_position = len(nums) - 1
    for i in range(len(nums) - 2, -1, -1):
        if i + nums[i] >= last_position:
            last_position = i

    return last_position == 0
    
if __name__ == "__main__":
    print(canJump([2,3,1,1,4]))
    print(canJump2([2,3,1,1,4]))