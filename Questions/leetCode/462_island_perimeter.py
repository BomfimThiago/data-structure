"""
You are given row x col grid representing a map where grid[i][j] = 1 represents land and grid[i][j] = 0 represents water.

Grid cells are connected horizontally/vertically (not diagonally). The grid is completely surrounded by water, 
and there is exactly one island (i.e., one or more connected land cells).

The island doesn't have "lakes", meaning the water inside isn't connected to the water around the island. 
One cell is a square with side length 1. The grid is rectangular, width and height don't exceed 100. Determine the perimeter of the island.

Example 1:


Input: grid = [[0,1,0,0],[1,1,1,0],[0,1,0,0],[1,1,0,0]]
Output: 16
Explanation: The perimeter is the 16 yellow stripes in the image above.
Example 2:

Input: grid = [[1]]
Output: 4
Example 3:

Input: grid = [[1,0]]
Output: 4
"""
from collections import deque
def islandPerimeter(grid):
    # grid[i][j] == 1 represent lands
    # grid[i][j] == 0 represent water
    # grids are connected horinzontalu/vertically, not diagonnaly(it means not bfs?)
    # the grid is surrounded by water, and there is only 1 island
    # each grid[i][j] has 1 length perimeter(area = 1)
    # determine the perimeter of the island(sum of all squares with 1)

    # so basically if the square is surrond by watter then I can add 1 

    ROWS, COLS = len(grid), len(grid[0])
    visited = set()

    def dfs(r, c):
        if r >= ROWS or r < 0 or c < 0 or c > COLS or grid[r][c] == 0:
            return 1
 
        if (r, c) in visited:
            return 0
        
        visited.add((r, c))
        perim = 0
        perim += dfs(r + 1, c)
        perim += dfs(r - 1, c)
        perim += dfs(r, c + 1)
        perim += dfs(r, c - 1)

        return perim
    
    # # basically I need to find the first land, to start counting
    for i in range(ROWS):
        for j in range(COLS):
            if grid[i][j]:
                return dfs(i, j)


if __name__ == "__main__":
    grid = [[0,1,0,0],[1,1,1,0],[0,1,0,0],[1,1,0,0]]
    print(islandPerimeter(grid))