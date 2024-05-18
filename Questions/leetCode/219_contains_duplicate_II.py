"""
Given an integer array nums and an integer k, return true if there are two distinct indices i and j 
in the array such that nums[i] == nums[j] and abs(i - j) <= k.

Example 1:

Input: nums = [1,2,3,1], k = 3
Output: true
Example 2:

Input: nums = [1,0,1,1], k = 1
Output: true
Example 3:

Input: nums = [1,2,3,1,2,3], k = 2
Output: false

"""
 
# brute approach, explode memory
def constainsNearByDuplicate(nums, k):
    # two distincts indices that are equal and the abs diff of the indices is <= k
    # ex [1, 2, 3, 1], k = 3,   i = 0, j = 3  abs(0 - 3) == 3 , 3 <= k, so is True

    # base case
    if not nums or len(nums) == 1:
        return False
    

    for i in range(len(nums)):
        l = i 
        r = i + 1
        while r < len(nums):
            if nums[l] == nums[r]:
                if abs(l - r) <= k:
                    return True
            r += 1
    return False
# Time Complexity 0(n2)
# Space Complexity O(1)

# using hash
def constainsNearByDuplicate2(nums, k):
    # base case
    if not nums or len(nums) == 1:
        return False
    
    hashNums = {}
    for i in range(len(nums)):
        if nums[i] not in hashNums: # 0 is considered False
            hashNums[nums[i]] = i # index
        else:
            j = hashNums[nums[i]]
            if abs(i - j) <= k:
                return True
            else:
                hashNums[nums[i]] = i # new index
    return False
# Time Complexity O(n)
# SpaceComplexity O(n) where n is the number of keys in hash , that in the worst case(the nums are uniques) is the same size of the array

# using sliciing widown, consider k as a window
# and then see if inside the window, there are equal numbers
def constainsNearByDuplicate3(nums, k):
    if not nums or len(nums) == 1 or k == 0:
        return False

    window = set() # the window will always have differents numbers
    l = 0

    for r in range(len(nums)):
        if r - l > k:
            window.remove(nums[l])
            l += 1

        if nums[r] in window:
            return True
        window.add(nums[r])

    return False
# Time Complexity O(n)
# SpaceComplexity O(k) since the window will store only k numbers maximum

if __name__ == "__main__":
    # print(constainsNearByDuplicate(nums = [1,2,3,1], k = 3))
    # print(constainsNearByDuplicate2(nums = [1,2,3,1], k = 3))
    print(constainsNearByDuplicate3(nums = [1,2,3,1], k = 3))
    