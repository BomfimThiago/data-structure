"""
217. Contains Duplicate
Solved
Easy
Topics
Companies
Given an integer array nums, return true if any value appears at least twice in the array, and return false if every element is distinct.


Example 1:

Input: nums = [1,2,3,1]
Output: true
Example 2:

Input: nums = [1,2,3,4]
Output: false
Example 3:

Input: nums = [1,1,1,3,3,4,3,2,4,2]
Output: true
 
"""
def containsDuplicate(nums):
    count = {}
    for n in nums:
        count[n] = count.get(n, 0) + 1
        if count[n] == 2:
            return True
        
    return False

# time complexit 0(n)
# space comlexity 0(1)

def containsDuplicate2(nums):
    seen = set()
    for n in nums:
        if n in seen:
            return True
        seen.add(n)

    return False

if __name__ == "__main__":
    print(containsDuplicate(nums = [1,1,1,3,3,4,3,2,4,2]))
    print(containsDuplicate2(nums = [1,1,1,3,3,4,3,2,4,2]))