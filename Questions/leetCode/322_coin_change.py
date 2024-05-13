"""
You are given an integer array coins representing coins of different denominations and an integer amount representing a total amount of money.

Return the fewest number of coins that you need to make up that amount. If that amount of money cannot be made up by any combination of the coins, return -1.

You may assume that you have an infinite number of each kind of coin.

Example 1:

Input: coins = [1,2,5], amount = 11
Output: 3
Explanation: 11 = 5 + 5 + 1
Example 2:

Input: coins = [2], amount = 3
Output: -1
Example 3:

Input: coins = [1], amount = 0
Output: 0

"""
# This is depth first search and for this kind of problems it explodes, even with cache
def coinChange(coins, amount):
    minC = float("inf")
    def dfs(i, totalVal, totalCoins, cache):
        nonlocal minC

        if (totalCoins, totalVal) in cache:
            return
        
        if totalVal == amount:
            minC = min(minC, totalCoins)
            return
        elif totalVal > amount:
            return

        if i < len(coins):
            totalCoins += 1
            dfs(i, totalVal + coins[i], totalCoins, cache)
            cache.add((totalCoins, totalVal + coins[i]))

            totalCoins -= 1
            dfs(i + 1, totalVal, totalCoins, cache)

    dfs(0, 0, 0, set())
    return minC if minC != float("inf") else -1

def coinChange2(coins, amount):
    dp = [float("inf")] * (amount + 1) # create an array of inf elements with size amount + 1, we are going to keep the min number of coins to reach amount from 0
    dp[0] = 0 # number de coins to reach amount 0 is 0
    # for coins = [1, 2, 3] , the number of coins to reach 1 is 1 given by dp[1] = 1, to reach 4 is 2 (2,2) or (3, 1) so dp[4] = 2 is the minimum number of coins to reach 
    # that amount, we are going to do this until we get the final amount

    for coin in coins: 
        for i in range(coin, amount + 1): # we want to work with each value pf dp
            dp[i] = min(dp[i], dp[i - coin] + 1)

    return dp[amount] if dp[amount] != float("inf") else -1


if __name__ == "__main__":
    print(coinChange2([3,7,405,436], 8839))
    print(coinChange2([2], 3))