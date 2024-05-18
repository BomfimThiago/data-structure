"""
You are given a sorted array consisting of only integers where every element appears exactly twice, except for one element which appears exactly once.

Return the single element that appears only once.

Your solution must run in O(log n) time and O(1) space.

 

Example 1:

Input: nums = [1,1,2,3,3,4,4,8,8]
Output: 2
Example 2:

Input: nums = [3,3,7,7,10,11,11]
Output: 10

"""
def singleNonDuplicate(nums):
    # for each number in the search see if the adjacents are equal
    while len(nums) != 1:
        m = len(nums) // 2


        if nums[m] == nums[m - 1]:
            if len(nums[:m - 1]) % 2 != 0:
                nums = nums[:m - 1]
            else:
                nums = nums[m + 1:]
        elif nums[m] == nums[m + 1]:
            if len(nums[:m]) % 2 != 0:
                nums = nums[:m]
            else:
                nums = nums[m + 2:]
        else:
            return nums[m]
        
    return nums[0]
if __name__ == "__main__":
    print(singleNonDuplicate([3,3,7,7,10,11,11]))