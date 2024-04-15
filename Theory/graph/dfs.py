"""
Question:
Count the uniquest paths from the top left to the bottom right. A single path may only move alonge
0s and can't visit the same cell more then once
matrix = [[0, 0, 0, 0],
          [1, 1, 0, 0],
          [0, 0, 0, 1],
          [0, 1, 0, 0].
          [0, 0, 0, 0]]
"""
def dfs(grid, r, c, visit):
    ROWS, COLS = len(grid), len(grid[0])

    if r == ROWS - 1 and c == COLS -1:
        return 1
    
    if (r < 0 or c < 0) or (r == ROWS or c == COLS) or (r, c) in visit or  grid[r][c] == 1:
        return 0

    visit.add((r, c))
    count = 0

    count += dfs(grid, r + 1, c, visit)
    count += dfs(grid, r - 1, c, visit)
    count += dfs(grid, r, c + 1, visit)
    count += dfs(grid, r, c - 1, visit)

    visit.remove((r, c))
    return count

if __name__ == "__main__":
    matrix = [[0, 0, 0, 0],
          [1, 1, 0, 0],
          [0, 0, 0, 1],
          [0, 1, 0, 0],
          [0, 0, 0, 0]] 
    print(dfs(matrix, 0, 0, set())) 