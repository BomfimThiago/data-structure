"""
Given n non-negative integers representing an elevation map where the width of each bar is 1, 
compute how much water it can trap after raining.

Example 1:

Input: height = [0,1,0,2,1,0,1,3,2,1,2,1]
Output: 6
Explanation: The above elevation map (black section) is represented
by array [0,1,0,2,1,0,1,3,2,1,2,1]. In this case, 6 units of rain water 
(blue section) are being trapped.

"""
from typing import List

# O(n) time complexity and O(n) space memory
def trap(height: List[int]) -> int:
    maxLeft = {}
    maxRight = {}
    minLR = {}

    maxWater = 0

    for i in range(len(height)):
        if i > 0:
            maxLeft[i] = max(height[:i])
        else:
            maxLeft[i] = 0
        
        if i < len(height) - 1:
            maxRight[i] = max(height[i+1:])
        else:
            maxRight[i] = 0

        minLR[i] = min(maxLeft[i], maxRight[i])

    for i in range(len(height)):
        maxWater += max(0, minLR[i] - height[i])

    return maxWater

# O(n) time complexity and O(1) space memory
def trap2(height: List[int]) -> int:
    if not height: return 0
    l, r = 0, len(height) - 1
    leftMax, rightMax = height[l], height[r]

    maxWater = 0

    while l < r:
        if leftMax < rightMax:
            l += 1
            leftMax = max(leftMax, height[l])
            maxWater += leftMax - height[l]
        else:
            r -= 1
            rightMax = max(rightMax, height[r])
            maxWater += rightMax - height[r]

    return maxWater


if __name__ == "__main__":
    print(trap([0,1,0,2,1,0,1,3,2,1,2,1]))
    print(trap2([0,1,0,2,1,0,1,3,2,1,2,1]))
