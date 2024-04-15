"""
Count the number of unique paths from the top left to the bottom right. You are only allowed to move down or to the right
matrix[3x3]
"""

def dfs(matrix, r, c, cache):
    ROWS, COLS = len(matrix), len(matrix[0])

    if r == ROWS or c == COLS:
        return 0
    
    if cache[r][c] > 0:
        return cache[r][c]
    
    cache[r][c] = dfs(matrix, r+1, c, cache) + dfs(matrix, r, c-1, cache)

    return cache[r][c]

    
    


