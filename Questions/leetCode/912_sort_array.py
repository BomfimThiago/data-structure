"""
Given an array of integers nums, sort the array in ascending order and return it.

You must solve the problem without using any built-in functions in O(nlog(n)) 
time complexity and with the smallest space complexity possible.


Example 1:

Input: nums = [5,2,3,1]
Output: [1,2,3,5]
Explanation: After sorting the array, the positions of some numbers are not changed (for example, 2 and 3), while the positions of other numbers are changed (for example, 1 and 5).
Example 2:

Input: nums = [5,1,1,2,0,0]
Output: [0,0,1,1,2,5]
Explanation: Note that the values of nums are not necessairly unique.

"""
# inplace sort algorithm
def insertionSort(nums):
    """
    We have to start with second element of the array as first element in the array is assumed to be sorted.
    Compare second element with the first element and check if the second element is smaller then swap them.
    Move to the third element and compare it with the second element, then the first element and swap as necessary to put it in the correct position among the first three elements.
    Continue this process, comparing each element with the ones before it and swapping as needed to place it in the correct position among the sorted elements.
    Repeat until the entire array is sorted.
    """
    l = 0
    for r in range(1, len(nums)):
        i = l
        j = r
        while i >= 0 and nums[j] < nums[i]:
            nums[i], nums[j] = nums[j], nums[i]
            i -= 1
            j -= 1
        l += 1

    return nums
# Time Complexity: O(n2)
# Space Complexity: O(1)

def bubbleSort(nums):
    """
    In Bubble Sort algorithm, 
    traverse from left and compare adjacent elements and the higher one is placed at right side. 
    In this way, the largest element is moved to the rightmost end at first. 
    This process is then continued to find the second largest and place it and so on until the data is sorted.
    """
    n = len(nums)
    for i in range(n):
        for j in range(0, n-i-1):
            if nums[j] > nums[j+1]:
                nums[j], nums[j+1] = nums[j+1], nums[j]
    return nums
        

def selectionsort(nums):
    for i in range(len(nums)):
        for j in range(i + 1, len(nums)):
            if nums[i] > nums[j]:
                nums[i], nums[j] = nums[j], nums[i]
    return nums

def mergesort(arr, l, r):
    def merge(arr, l, m , r):
        print("l", l)
        print("m", m)
        print("r", r)
        
        L = arr[l:m + 1]
        R = arr[m + 1:r+1]
        n1 = len(L)
        n2 = len(R)

        i = 0
        j= 0
        k = l
        while i < n1 and j < n2:
            if L[i] <= R[j]:
                arr[k] = L[i]
                i += 1
            else:
                arr[k] = R[j]
                j += 1
            k += 1

        while i < n1:
            arr[k] = L[i]
            i += 1
            k += 1

        while j < n2:
            arr[k] = R[j]
            j += 1
            k += 1

    if l < r:
        m = l + (r - l) // 2
        mergesort(arr, l, m)
        mergesort(arr, m + 1, r)
        merge(arr, l, m , r)

    return arr

if __name__ == "__main__":
    arr = [4, 2, 8, 6, 1, 5, 9, 3, 7]
    l = 0
    r = len(arr) - 1
    print(mergesort(arr, l, r)) 