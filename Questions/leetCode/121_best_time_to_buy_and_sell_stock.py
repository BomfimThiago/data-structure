"""
You are given an array prices where prices[i] is the price of a given stock on the ith day.

You want to maximize your profit by choosing a single day to buy one stock and choosing a different day in the future to sell that stock.

Return the maximum profit you can achieve from this transaction. If you cannot achieve any profit, return 0.


Example 1:

Input: prices = [7,1,5,3,6,4]
Output: 5
Explanation: Buy on day 2 (price = 1) and sell on day 5 (price = 6), profit = 6-1 = 5.
Note that buying on day 2 and selling on day 1 is not allowed because you must buy before you sell.
Example 2:

Input: prices = [7,6,4,3,1]
Output: 0
Explanation: In this case, no transactions are done and the max profit = 0.
"""
from typing import List
xw
# Another way is to track the min of the left array prices[:i] in each loop
def maxProfit2(prices: List[int]) -> int:
    maxP = 0
    minL = prices[0]
    for i in range(1, len(prices)):
        buy = minL
        sell = prices[i]

        maxP = max(maxP, sell - buy)
        minL = min(minL, prices[i])

    return maxP
# two pointers
def maxProfit(prices):
    # base cases
    if len(prices) == 0 or len(prices) == 1:
        return 0

    l = 0 # l means buy
    r = 1 # r means sell
    maxP = 0
    while r < len(prices):
        if prices[l] < prices[r]:
            p = prices[r] - prices[l] # sell - buy
            maxP = max(maxP, p)
        else:
            l = r

        r += 1

    return maxP

# Time Complexity is O(n) where n is the size of the array prices
# Space Complexity is O(1)


if __name__ == "__main__":
    print(maxProfit([7,6,4,3,1]))
    # print(maxProfit2([7,1,5,3,6,4]))
    # print(maxProfit3([7,1,5,3,6,4]))