"""
You are given an m x n integer array grid. There is a robot initially located at the top-left corner (i.e., grid[0][0]). 
The robot tries to move to the bottom-right corner (i.e., grid[m - 1][n - 1]). The robot can only move either down or right at any point in time.

An obstacle and space are marked as 1 or 0 respectively in grid. A path that the robot takes cannot include any square that is an obstacle.

Return the number of possible unique paths that the robot can take to reach the bottom-right corner.

The testcases are generated so that the answer will be less than or equal to 2 * 109.
"""
def uniquePathsWithObstacles(grid):
    ROWS, COLS = len(grid), len(grid[0])

    def dfs(r, c, cache):
        if r < 0 or r >= ROWS or c < 0 or c >= COLS \
            or grid[r][c] == 1:
            return 0
        
        if r == ROWS -1 and c == COLS - 1:
            return 1
        
        if (r, c) in cache:
            return cache[(r, c)]
        
        count = 0

        count += dfs(r + 1, c, cache)
        count += dfs(r, c + 1, cache)

        cache[(r, c)] = count

        return cache[(r, c)]
    return dfs(0, 0, {})

if __name__ == "__main__":
    obstacleGrid = [[0,0,0],[0,1,0],[0,0,0]]
    print(uniquePathsWithObstacles(obstacleGrid))