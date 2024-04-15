"""
Given an integer array nums and an integer k, return the k most frequent elements. You may return the answer in any order.
Example 1:

Input: nums = [1,1,1,2,2,3], k = 2
Output: [1,2]
Example 2:

Input: nums = [1], k = 1
Output: [1]

"""
from typing import List

# with heap would be better(klogn) but with bucket sort we can do in O(n)
def topKFrequent(nums: List[int], k: int) -> List[int]:
        # +1 because we theorically dont want the indice 0 on our bucket so if the nums has length 2
        # our bucket will have the indices 0 1 2(length 3)
        # remember each index of our bucket represent number of times a number is frequent
        # so in index 1 of our bucket we gonna put all the numbers in nums which appears once and so on
        bucket = [[] for _ in range(len(nums) + 1)]
        count = {}
        for n in nums:
            count[n] = 1 + count.get(n, 0)

        for n, c in count.items():
            bucket[c].append(n) # each value is the number of times the number k appears, so v becomes an indice in our bucket

        res = [] # must have the size o k
        for i in range(len(bucket) - 1, 0, -1):
            for item in bucket[i]:
                res.append(item)
                if len(res) == k:
                    return res

if __name__ == "__main__":
    print(topKFrequent([1,1,1,2,2,3], 2))