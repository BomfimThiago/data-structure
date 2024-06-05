"""
You are given a 0-indexed integer array nums and an integer p. 
Find p pairs of indices of nums such that the maximum difference amongst all the pairs is minimized. 
Also, ensure no index appears more than once amongst the p pairs.

Note that for a pair of elements at the index i and j, the difference of this pair is |nums[i] - nums[j]|, 
where |x| represents the absolute value of x.

Return the minimum maximum difference among all p pairs. We define the maximum of an empty set to be zero.

 

Example 1:

Input: nums = [10,1,2,7,1,3], p = 2
Output: 1
Explanation: The first pair is formed from the indices 1 and 4, and the second pair is formed from the indices 2 and 5. 
The maximum difference is max(|nums[1] - nums[4]|, |nums[2] - nums[5]|) = max(0, 1) = 1. Therefore, we return 1.
Example 2:

Input: nums = [4,2,1,2], p = 1
Output: 0
Explanation: Let the indices 1 and 3 form a pair. The difference of that pair is |2 - 2| = 0, 
which is the minimum we can attain.
"""
def minimizeMax(nums, p):
    # if I sort the elements, the neighbours will always give me the min difference
    # greedy dp start at the beggning of the array
    # after sort
    nums.sort()

# binary search
def minimizeMax2(nums, p):
    if p == 0:
        return 0

    nums.sort() # is to be Greedy
    res = max(nums) - min(nums) 
    l, r = 0, max(nums) - min(nums) # this is my max diff, I'm gonna try to search between this range

    def isValid(threshold):
        i, count = 1, 0
        while i < len(nums):
            if nums[i] - nums[i - 1] <= threshold:
                count += 1
                i += 2
            else:
                i += 1

            if count == p:
                return True
            
        return False

    while l <= r:
        m = l + (r - l) // 2 # this is to avoid overflow
        if isValid(m):
            res = m
            r = m - 1
        else:
            l = m + 1

    return res


if __name__ == "__main__":
    nums = [4,0,2,1,2,5,5,3]
    p = 3
    nums2 = [10,1,2,7,1,3]
    p2 = 2
    nums3 = [4,2,1,2]
    p3 = 1
    print(minimizeMax2(nums3, p3))