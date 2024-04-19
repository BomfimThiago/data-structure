"""
You are climbing a staircase. It takes n steps to reach the top.

Each time you can either climb 1 or 2 steps. In how many distinct ways can you climb to the top?
"""
def climbStairs(n: int):
    # not efficient
    def dfs(step, cache):
        if step == n:
            return 1

        if step > n or step in cache:
            return 0
        
        count = 0

        cache.add(step)
        count += dfs(step + 1, cache)
        count += dfs(step + 2, cache)
        cache.remove(step)
        

        return count
    
    return dfs(0, set())

# true dynamic programming
def climbStairs2(n: int):
    one, two = 1, 1
    for i in range(n - 1):
        tmp = one
        one = one + two
        two = tmp
    return one

if __name__ == "__main__":
    print(climbStairs(5))
    print(climbStairs2(5))