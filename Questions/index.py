
def uniquePaths(m: int, n: int) -> int:
    ROWS, COLS = m, n
    # because I just can go down or right
    # the number of the ways from in the last column
    # and the last row will be always be 1
    grid = [[0] * COLS for _ in range(ROWS)]

    for i in range(ROWS):
        grid[i][-1] = 1

    for i in range(COLS):
        grid[-1][i] = 1

    for i in range(ROWS - 2, -1, -1):
        for j in range(COLS - 2, -1 , -1):
            grid[i][j] = grid[i + 1][j] + grid[i][j + 1]

    return grid[0][0]

if __name__ == "__main__":
    print(uniquePaths(5, 3))