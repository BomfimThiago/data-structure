"""
Given an integer array nums, return an array answer such that answer[i] is equal to the product of all the elements of nums except nums[i].

The product of any prefix or suffix of nums is guaranteed to fit in a 32-bit integer.

You must write an algorithm that runs in O(n) time and without using the division operation.

"""

def productExceptSelf(nums):
    n = len(nums)
    result = [1] * n
    left = 1
    right = 1

    print(f'Initial state: {result}')

    for i in range(n):
        result[i] *= left
        result[n - 1 - i] *= right
        left *= nums[i]
        right *= nums[n - 1 - i]

        print(f'After iteration {i}: {result}, left: {left}, right: {right}')
    
    return result

print(productExceptSelf([1, 2, 3, 4]))
