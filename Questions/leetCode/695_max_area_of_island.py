"""
You are given an m x n binary matrix grid. An island is a group of 1's (representing land) 
connected 4-directionally (horizontal or vertical.) You may assume all four edges of the grid are surrounded by water.

The area of an island is the number of cells with a value 1 in the island.

Return the maximum area of an island in grid. If there is no island, return 0.

Example 1:


Input: grid = [[0,0,1,0,0,0,0,1,0,0,0,0,0],[0,0,0,0,0,0,0,1,1,1,0,0,0],
[0,1,1,0,1,0,0,0,0,0,0,0,0],[0,1,0,0,1,1,0,0,1,0,1,0,0],[0,1,0,0,1,1,0,0,1,1,1,0,0],
[0,0,0,0,0,0,0,0,0,0,1,0,0],[0,0,0,0,0,0,0,1,1,1,0,0,0],[0,0,0,0,0,0,0,1,1,0,0,0,0]]
Output: 6
Explanation: The answer is not 11, because the island must be connected 4-directionally.
Example 2:

Input: grid = [[0,0,0,0,0,0,0,0]]
Output: 0

"""
from collections import deque
def maxAreaIsland(grid):
    # binary matrix 0 or 1
    # islands is group of 1s
    # return the maxArea
    maxA = 0
    ROWS, COLS = len(grid), len(grid[0])
    visited = set()
    def bfs(row, col):
        q = deque()
        area = 0
        q.append((row, col))

        while q:
            r, c = q.popleft()
            neighbours = [[r + 1, c], [r - 1, c], [r, c + 1], [r, c - 1]]

            for nr, nc in neighbours:
                if nr >= 0 and nr < ROWS and nc >= 0 and nc < COLS and (nr, nc) not in visited and grid[nr][nc] == 1:
                    area += 1
                    q.append((nr, nc))
                    visited.add((nr, nc))
        return area
    
    for i in range(ROWS):
        for j in range(COLS):
            if grid[i][j] == 1 and grid[i][j] not in visited:
                area = bfs(i, j)
                area = area if area > 0 else 1
                maxA = max(area, maxA)

    return maxA

if __name__ == "__main__":
    grid = [
        [0,0,1,0,0,0,0,1,0,0,0,0,0],
        [0,0,0,0,0,0,0,1,1,1,0,0,0],
        [0,1,1,0,1,0,0,0,0,0,0,0,0],
        [0,1,0,0,1,1,0,0,1,0,1,0,0],
        [0,1,0,0,1,1,0,0,1,1,1,0,0],
        [0,0,0,0,0,0,0,0,0,0,1,0,0],
        [0,0,0,0,0,0,0,1,1,1,0,0,0],
        [0,0,0,0,0,0,0,1,1,0,0,0,0]
    ]
    grid2 = [[1]]
    print(maxAreaIsland(grid2))