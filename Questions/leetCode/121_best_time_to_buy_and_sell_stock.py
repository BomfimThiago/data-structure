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

# this works but it explode the memory
def maxProfit(prices: List[int]) -> int:
    maxP = 0
    for i in range(1, len(prices)):
        # min do left array seria o dia da venda
        buy = min(prices[:i])
        sell = prices[i]

        maxP = max(maxP, sell- buy)

    return maxP
        
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

# Two pointers solutions
def maxProfit3(prices: List[int]) -> int:
    l, r = 0, 1 #left=buy, right=sell
    maxP = 0

    while r < len(prices):
        if prices[l] < prices[r]:
            p = prices[r] - prices[l]
            maxP = max(maxP, p)
        else:
            l = r
        r += 1

    return maxP



if __name__ == "__main__":
    print(maxProfit([7,1,5,3,6,4]))
    print(maxProfit2([7,1,5,3,6,4]))
    print(maxProfit3([7,1,5,3,6,4]))