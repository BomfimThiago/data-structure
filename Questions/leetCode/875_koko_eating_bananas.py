"""
Koko loves to eat bananas. There are n piles of bananas, the ith pile has piles[i] bananas. The guards have gone and will come back in h hours.

Koko can decide her bananas-per-hour eating speed of k. Each hour, she chooses some pile of bananas and eats k bananas from that pile. If the pile has less than k bananas, she eats all of them instead and will not eat any more bananas during this hour.

Koko likes to eat slowly but still wants to finish eating all the bananas before the guards return.

Return the minimum integer k such that she can eat all the bananas within h hours.

Example 1:

Input: piles = [3,6,7,11], h = 8
Output: 4
Example 2:

Input: piles = [30,11,23,4,20], h = 5
Output: 30
Example 3:

Input: piles = [30,11,23,4,20], h = 6
Output: 23

"""
from typing import List
import math


def minEatingSpeed(piles: List[int], h: int) -> int:
    maxN = max(piles)
    l = 1 # k pode ser no minimo 1
    r = maxN # k pode ser no maximo maxN
    minK = r
    while l <= r:
        k = (l + r) // 2

        hours = sum([math.ceil(num/k) for num in piles])

        if hours > h:
            l = k + 1
        else:
            r = k - 1
            minK = min(minK, k)

    return minK

if __name__ == "__main__":
    print(minEatingSpeed([3,6,7,11], 8))