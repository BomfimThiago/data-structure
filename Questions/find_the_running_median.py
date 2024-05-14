"""
given an input stream of n integers, perfome the following task for each ith integer
1 - add the iTh to a running list of integers
2 - find the median of the update running list
3 - print eh updated median on a new line. the value must be double-precision number scaled to 1 decimal place.
ex. a = [7, 3, 5, 2]
prints:
[7] median 7.0
[3, 7] median 5.0
[3, 5, 7] median 5.0
[2, 3, 5, 7] median 4.0
"""

from heapq import heappop, heappush

class Median:
    def __init__(self):
        self.small, self.large = [], []

    def insert(self, num):
        # push to the max heap and swap with min heap if needed
        heappush(self.small, -1 * num)
        # if the top of the maxHead is greater then top of the minHeap
        # we pop form the maxHeap and add in the minHeap
        if(self.small and self.large and (-1 * self.small[0] > self.large[0])):
            val = -1 * heappop(self.small)
            heappush(self.large, val)

        if len(self.small) > len(self.large) + 1: # we change again, the diff can be only 1
            val = -1 * heappop(self.small)
            heappush(self.large, val)

        if len(self.large) > len(self.small) + 1:
            val = heappop(self.large)
            heappush(self.small, -1 * val)

    def get_median(self):
        if len(self.small) > len(self.large):
            return f"{-1 * self.small[0]}.1f"
        elif len(self.large) > len(self.small):
            return f"{self.large[0]}.1f"
        
        return f"{(-1 * self.small[0] + self.large[0]) / 2}.2f"


def runningMedian(a):
    # idea is to having two heaps, 1 min e 1 max.
    # design a class that arbitraty insert e also we have the getMedian
    # in the beggning add the first value to the maxHeap
    # from the second value on, we want that the both heaps being balanced
    # if the length of the 2 heaps are equal, then we have a pair median, we
    # need to get the top of then , add and divide by 2
    # as long as the difference is one , then thats okay
    medianFinder = Median()
    medians = []
    for n in a:
        medianFinder.insert(n)
        median = medianFinder.get_median()
        medians.append(median)
    return medians
    

if __name__ == "__main__":
    print(runningMedian([7, 3, 5, 2]))