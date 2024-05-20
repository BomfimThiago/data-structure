"""
You are given an integer array cost where cost[i] is the cost of ith step on a staircase. 
Once you pay the cost, you can either climb one or two steps.

You can either start from the step with index 0, or the step with index 1.

Return the minimum cost to reach the top of the floor.

 

Example 1:

Input: cost = [10,15,20]
Output: 15
Explanation: You will start at index 1.
- Pay 15 and climb two steps to reach the top.
The total cost is 15.
Example 2:

Input: cost = [1,100,1,1,1,100,1,1,100,1]
Output: 6
Explanation: You will start at index 0.
- Pay 1 and climb two steps to reach index 2.
- Pay 1 and climb two steps to reach index 4.
- Pay 1 and climb two steps to reach index 6.
- Pay 1 and climb one step to reach index 7.
- Pay 1 and climb two steps to reach index 9.
- Pay 1 and climb one step to reach the top.
The total cost is 6.
 
"""
# top-down
def minCostClimbingStairs(stairs):
    def dfs(i, cache):
        if i >= len(stairs):
            return 0
        
        if i in cache:
            return cache[i]
        
        take_1_step = stairs[i] + dfs(i + 1, cache)
        take_2_steps = stairs[i] + dfs(i + 2, cache)

        cache[i] = min(take_1_step, take_2_steps)

        return cache[i]
            
    return min(dfs(0, {}), dfs(1, {}))

# bottom-up
def minCostClimbingStairs2(cost):
    take_one_step = 0
    take_two_steps = 0
    d = {} # vai guardar o mínimo em cada posicao
    for i in range(len(cost) - 1, -1, -1):
        d[i] = min(cost[i] + take_one_step, cost[i] + take_two_steps)
        tmp = take_one_step
        take_one_step = d[i]
        take_two_steps = tmp

    return min(d[0], d[1])

if __name__ == "__main__":
    cost = [10, 15, 20]
    print(minCostClimbingStairs(cost))
    print(minCostClimbingStairs2(cost))