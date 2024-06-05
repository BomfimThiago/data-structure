"""
Given an array arr[] of size N, the task is to printing K largest elements in an array.
Note: Elements in output array can be in any order
"""
# Time complexity: O(n * log (mx-mn)), where mn be minimum and mx be maximum element of array.
# Auxiliary Space: O(1)

def largestKElement(arr, k):
    # binary search between the min and max value
    low = float("inf")
    high = float("inf")
    n = len(arr)
    for i in range(len(arr)):
        low = min(arr[i], low)
        high = max(arr[i], high)

    while low < high:
        mid = (low + high) / 2
        count = 0

        # count how much elements greater then the mid value
        for i in range(n):
            if arr[i] > mid:
                count += 1

        # If there are at least K elements greater than mid, search the right half
        if count >= k:
            low = mid + 1
        # Otherwise, search the left half
        else:
            high = mid - 1
    return high


# heap is the more efficient way
# Time complexity: O(n * log k)
# Auxiliary Space: O(1)

import heapq

def k_largest_elements(arr, k):
    if k == 0:
        return []
    
    # Use heapq to create a min-heap with the first k elements
    min_heap = arr[:k]
    heapq.heapify(min_heap)
    
    # Iterate through the remaining elements
    for num in arr[k:]:
        # If the current number is larger than the smallest element in the heap
        if num > min_heap[0]:
            # Replace the smallest element with the current number
            heapq.heapreplace(min_heap, num)
    
    # The heap now contains the k largest elements
    return min_heap
