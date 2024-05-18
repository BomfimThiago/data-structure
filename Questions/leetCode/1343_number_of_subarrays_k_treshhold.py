"""
Given an array of integers arr and two integers k and threshold, 
return the number of sub-arrays of size k and average greater than or equal to threshold.

Input: arr = [2,2,2,2,5,5,5,8], k = 3, threshold = 4
Output: 3
Explanation: Sub-arrays [2,5,5],[5,5,5] and [5,5,8] have averages 4, 5 and 6 respectively. All other sub-arrays of size 3 have averages less than 4 (the threshold).
Example 2:

Input: arr = [11,13,17,23,29,31,7,5,2,3], k = 3, threshold = 5
Output: 6
Explanation: The first 6 sub-arrays of size 3 have averages greater than 5. Note that averages are not integers.
"""
def numOfSubarrays(arr, k, threshold):
    if not arr or k == 0:
        return 0


    l = 0
    r = k - 1
    maxC = 0
    currAmount = sum(arr[l:r])

    while r < len(arr): # O(n)
        currAmount += arr[r]
        if currAmount / k >= threshold: # see if there is any decimal problem
            maxC += 1

        # update currAmount
        currAmount -= arr[l]

        # moving the window
        l += 1
        r += 1


    return maxC
# Time Complexity O(n)
# Space Complexity O(1)

if __name__ == "__main__":
    print(numOfSubarrays(arr = [11,13,17,23,29,31,7,5,2,3], k = 3, threshold=5))