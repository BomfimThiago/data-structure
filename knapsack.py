"""
A knapsack is defined as a bag carried by hikers or soldiers for carrying food, clothes, and other belongings. 
The Knapsack problem, as the name suggests, is the problem faced by a person who has a knapsack with a limited 
capacity and wants to carry the most valuable items. In other words, we are given items, 
each having a specific weight and a value, and a knapsack with a maximum capacity. Our job is to put as many 
items as possible in the knapsack such that the cumulative weight of the items doesn't exceed the knapsack's capacity, 
and the cumulative value of the items in the knapsack is maximized.

8 types of knapsacks problems
- 0/1 Knapsack
- Target Sum
- Subset Sum
- Count of Subset Sum
- Minimum Subarray Sum Difference
- Minimunm Number of Refueling Stops
- Equal Sum Subarrays
- Count Square Submatrices

The 0/1 Knapsack is a special case of the Knapsack problem where item selection has some constraints. In general, the following restrictions are applied:

A maximum of one item can be selected of each kind, that is, the number of items of each kind in the knapsack is either zero or one.

We can't take a fraction of an item, that is, we either have to take the complete item or leave it.
"""

# naive implementation in python
# this implementation has time complexity is O(2ˆn)
# This is because we have two possible choices every time, either to include the item or not.

from typing import List

def knapSack(W: int, wt: List[int], val:  List[int], n: int):
    """
    W: maximum weight of the sack
    wt: list of weights for the items
    val: list of items
    n: size of the lists
    """

    # Base Case
    if n == 0 or W == 0:
        return 0
    
    # If weight of the nth item is 
    # more than Knapsack of capacity W, 
    # then this item cannot be included 
    # in the optimal solution 
    if(wt[n-1] > W):
        return knapSack(W, wt, val, n-1)
    else:
        # return the maximum of two cases: 
        # (1) nth item included 
        # (2) not included
        return max(
            val[n-1] + knapSack(W - wt[n-1], wt, val, n-1),
            knapSack(W, wt, val, n-1)
        )
    
# Driver Code 
if __name__ == '__main__': 
    profit = [60, 100, 120] 
    weight = [10, 20, 30] 
    W = 50
    n = len(profit) 
    print(knapSack(W, weight, profit, n))


# optimized solution Top-down solution
"""
Top-down solution
The top-down solution, commonly known as the memoization technique, is an enhancement of the recursive solution. 
It overcomes the problem of calculating redundant solutions over and over again by storing them in a table.

In the recursive approach, the two variables that kept changing in each call were the total weight of the knapsack 
and the number of items we had. So, we’ll use these two variables to define each distinct subproblem. 
Therefore, we need a 2-D array to store these values and the result of any given subproblem when we encounter 
it for the first time. At any later time, if we encounter the same sub-problem, 
we can return the stored result from the table with an 

O(1) lookup instead of recalculating that subproblem.

Let’s implement the algorithm as discussed above:
"""
def knapSack(W: int, wt: List[int], val:  List[int], n: int):
    """
    W: maximum weight of the sack
    wt: list of weights for the items
    val: list of items
    n: size of the lists
    matrix is a variable created to store a already test possibly
    so if I already used knapSack with the same arguments, we dont need
    to calculate again we just pass to the next evaluation
    """
    # Base Case
    if n == 0 or W == 0:
        return 0
    
    if matrix[n][W] != -1:
        return matrix[n][W]
    
    if wt[n-1] <= W:
        matrix[n][W] = max(
            val[n-1] + knapSack(
                W - wt[n-1], wt, val, n-1
            ),
                knapSack(W, wt, val, n-1)
            )
        
        return matrix[n][W]
    elif wt[n-1] > W:
        matrix[n][W] = knapSack(wt, val, W, n-1)
        return matrix[n][W]
    
# Driver code 
if __name__ == '__main__': 
    profit = [60, 100, 120] 
    weight = [10, 20, 30] 
    W = 50
    n = len(profit) 
      
    # We initialize the matrix with -1 at first. 
    matrix = [[-1 for i in range(W + 1)] for j in range(n + 1)] 
    print(knapSack(W, weight, profit, n)) 
  

# bottom-up solution
def knapSack(W, wt, val, n): 
    K = [[0 for x in range(W + 1)] for x in range(n + 1)] 
  
    # Build table K[][] in bottom up manner 
    for i in range(n + 1): 
        for w in range(W + 1): 
            if i == 0 or w == 0: 
                K[i][w] = 0
            elif wt[i-1] <= w: 
                K[i][w] = max(val[i-1] 
                              + K[i-1][w-wt[i-1]], 
                              K[i-1][w]) 
            else: 
                K[i][w] = K[i-1][w] 
  
    return K[n][W] 
  
  
# Driver code 
if __name__ == '__main__': 
    profit = [60, 100, 120] 
    weight = [10, 20, 30] 
    W = 50
    n = len(profit) 
    print(knapSack(W, weight, profit, n)) 
  