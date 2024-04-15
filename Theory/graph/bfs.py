"""
question:
Find the length of the shortest path from the top left of the grid to the bottom right
matrix = [[0, 0, 0, 0],
          [1, 1, 0, 0],
          [0, 0, 0, 1],
          [0, 1, 0, 0]]
"""
from collections import deque

def bfs(grid):
    ROWS, COLS = len(grid), len(grid[0])
    visit = set()
    queue = deque()
    queue.append((0, 0)) # row = 0, col = 0
    visit.add((0, 0))

    count = 0

    while queue:
        for i in range(len(queue)):
            r, c = queue.popleft()

            if r == ROWS - 1 and c == COLS - 1:
                return count

            # nr is neighbour row, nc is neighbour col
            neighbours = [[r, c+1], [r, c-1], [r+1, c], [r-1, c]]
            for nr, nc in neighbours:
                if (nr < 0 or nc < 0) or (nr >= ROWS or nc >= COLS) or (nr, nc) in visit or grid[nr][nc] == 1:
                    continue # go to the next neighbour
                queue.append((nr, nc))
                visit.add((nr, nc))
        count += 1


if __name__ == "__main__":
    grid = [[0, 0, 0, 0],
        [1, 1, 0, 0],
        [0, 0, 0, 1],
        [0, 1, 0, 0]]
    
    print(bfs(grid))