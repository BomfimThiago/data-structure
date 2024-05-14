"""
Given an m x n 2D binary grid grid which represents a map of '1's (land) and '0's (water), return the number of islands.

An island is surrounded by water and is formed by connecting adjacent lands horizontally or vertically. You may assume all four edges of the grid are all surrounded by water.

Example 1:

Input: grid = [
  ["1","1","1","1","0"],
  ["1","1","0","1","0"],
  ["1","1","0","0","0"],
  ["0","0","0","0","0"]
]
Output: 1
Example 2:

Input: grid = [
  ["1","1","0","0","0"],
  ["1","1","0","0","0"],
  ["0","0","1","0","0"],
  ["0","0","0","1","1"]
]
Output: 3
"""
from collections import deque
def  numIslands(grid):
    if not grid:
        return 0
    
    ROWS, COLS = len(grid), len(grid[0])
    visited = set()
    islands = 0

    # go through this code just o mark visited or not in all adjacents
    # of 1
    def bfs(r, c):
        q = deque()
        visited.add((r, c))
        q.append((r,c))

        while q:
            row, col = q.popleft()
            neighbours = [[row + 1, col], [row - 1, col], [row, col + 1], [row, col - 1]]
            for nr, nc in neighbours:
                if (nr in range(ROWS)) and (nc in range(COLS)) and grid[nr][nc] == "1" and (nr, nc) not in visited:
                    q.append((nr, nc))
                    visited.add((nr, nc))


    for i in range(ROWS):
        for j in range(COLS):
            if grid[i][j] == "1" and (i, j) not in visited:
                bfs(i, j)
                islands += 1

    return islands


if __name__ == "__main__":
    img = [["1","1","1","1","0"],["1","1","0","1","0"],["1","1","0","0","0"],["0","0","0","0","0"]]
    print(numIslands(img))
