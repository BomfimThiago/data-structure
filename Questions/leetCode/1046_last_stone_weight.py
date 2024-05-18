"""
You are given an array of integers stones where stones[i] is the weight of the ith stone.

We are playing a game with the stones. On each turn, we choose the heaviest two stones and smash them together. 
Suppose the heaviest two stones have weights x and y with x <= y. The result of this smash is:

If x == y, both stones are destroyed, and
If x != y, the stone of weight x is destroyed, and the stone of weight y has new weight y - x.
At the end of the game, there is at most one stone left.

Return the weight of the last remaining stone. If there are no stones left, return 0.


"""
from heapq import heapify, heappop, heappush
def lastStoneWeight(stones):
    # we are going to build a max heap, in python to multiply each value by -1 stones = [stone * -1 for stone in stones]
    stones = [stone * -1 for stone in stones]
    heapify(stones) # max heap

    while len(stones) > 1:
        x = abs(heappop(stones))
        y = abs(heappop(stones))

        if y < x:
            diff = x - y
            heappush(stones, -1 * diff)

    stones.append(0)
    return abs(stones[0])


if __name__ == "__main__":
    print(lastStoneWeight([2,7,4,1,8,1]))