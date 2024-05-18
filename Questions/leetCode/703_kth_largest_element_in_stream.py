"""
Design a class to find the kth largest element in a stream. Note that it is the kth largest element in the sorted order, not the kth distinct element.

Implement KthLargest class:

KthLargest(int k, int[] nums) Initializes the object with the integer k and the stream of integers nums.
int add(int val) Appends the integer val to the stream and returns the element representing the kth largest element in the stream.

"""

# this structure is a heap, a min heap of size k
# we can add or pop in a heap in O(logn)
# we can search in a heap in 0(1)
from typing import List
from heapq import heapify, heappop, heappush


class KthLargest:
    def __init__(self, k: int, nums: List[int]):
        self.min_heap, self.k = nums, k
        heapify(self.min_heap)
        while len(self.min_heap) > k:
            heappop(self.min_heap)

    def add(self, val: int) -> int:
        heappush(self.min_heap, val)
        if len(self.min_heap) > self.k:
            heappop(self.min_heap)
        return self.min_heap[0]