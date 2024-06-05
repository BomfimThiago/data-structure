"""
Given an array of points where points[i] = [xi, yi] represents a point on the X-Y plane and an integer k, 
return the k closest points to the origin (0, 0).

The distance between two points on the X-Y plane is the Euclidean distance (i.e., √(x1 - x2)2 + (y1 - y2)2).

You may return the answer in any order. The answer is guaranteed to be unique (except for the order that it is in).

 

Example 1:


Input: points = [[1,3],[-2,2]], k = 1
Output: [[-2,2]]
Explanation:
The distance between (1, 3) and the origin is sqrt(10).
The distance between (-2, 2) and the origin is sqrt(8).
Since sqrt(8) < sqrt(10), (-2, 2) is closer to the origin.
We only want the closest k = 1 points from the origin, so the answer is just [[-2,2]].
Example 2:

Input: points = [[3,3],[5,-1],[-2,4]], k = 2
Output: [[3,3],[-2,4]]
Explanation: The answer [[-2,4],[3,3]] would also be accepted.
"""
from heapq import heappop, heappush, heappushpop, heapify
import math
# with heap
# Time Complexity n log k , Space Complexity O(k)
def kClosest(points, k):
    minHeap = [(float("-inf"), [float("inf"), float("inf")]) for _ in range(k)] # sqt, points

    for x, y in points:
        sqrt = math.sqrt(math.pow(x,2) + math.pow(y,2))
        if len(minHeap) < k:
            heappush(minHeap, (-sqrt, [x, y]))
        else:
            heappushpop(minHeap, (-sqrt, [x, y]))
    
    res = []
    for _ in range(k):
        sqrt, points = minHeap.pop()
        res.append(points)

    return res

def kClosest2(points, k):
    minHeap = []
    for x, y in points:
        dist = math.sqrt((x ** 2) + (y ** 2))
        minHeap.append([dist, x, y])

    heapify(minHeap)
    res = []
    while k > 0:
        dist, x, y = heappop(minHeap)
        res.append([x,y])
        k -= 1

    return res

if __name__ == "__main__":
    points = [[1,3],[-2,2]]
    k = 1
    points2 = [[3,3],[5,-1],[-2,4]] 
    k2 = 2
    print(kClosest(points2, k2))
    print(kClosest2(points2, k2))