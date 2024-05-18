"""
You are a hiker preparing for an upcoming hike. You are given heights, a 2D array of size rows x columns, 
where heights[row][col] represents the height of cell (row, col). You are situated in the top-left cell, (0, 0), 
and you hope to travel to the bottom-right cell, (rows-1, columns-1) (i.e., 0-indexed). You can move up, down, left, 
or right, and you wish to find a route that requires the minimum effort.

A route's effort is the maximum absolute difference in heights between two consecutive cells of the route.

Return the minimum effort required to travel from the top-left cell to the bottom-right cell.


Example 1:

Input: heights = [[1,2,2],[3,8,2],[5,3,5]]
Output: 2
Explanation: The route of [1,3,5,3,5] has a maximum absolute difference of 2 in consecutive cells.
This is better than the route of [1,2,2,2,5], where the maximum absolute difference is 3.
Example 2:

Input: heights = [[1,2,3],[3,8,4],[5,3,5]]
Output: 1
Explanation: The route of [1,2,3,4,5] has a maximum absolute difference of 1 in consecutive cells, which is better than route [1,3,5,3,5].
Example 3:


Input: heights = [[1,2,1,1,1],[1,2,1,2,1],[1,2,1,2,1],[1,2,1,2,1],[1,1,1,2,1]]
Output: 0
Explanation: This route does not require any effort.
"""

# a lot of graph problems its better to create an adj list
# but here we can just create a heap since its a grid
from heapq import heappop, heappush, heapify
def minimumEffortPath(heights):
    ROWS, COLS = len(heights), len(heights[0])
    min_heap = [[0, 0, 0]] # [diff, r, c] because we want to prioritize, start at the top-left
    visited = set()
    while min_heap:
        # its guaranted to reach the bottom-down cell, so we can return values inside the while
        diff, r, c = heappop(min_heap)

        if (r, c) in visited:
            continue

        visited.add((r, c))

        if (r, c) == (ROWS -1, COLS - 1): # we reach the final
            return diff # seria o max diff para esta rota

        neighbours = [[r + 1, c], [r -1, c], [r, c + 1], [c, r - 1]]
        for nr, nc in neighbours:
            if nr < 0 or nc < 0 or nr >= ROWS or nc >= COLS or (nr, nc) in visited:
                continue

            new_diff = max(diff, abs(heights[r][c] - heights[nr][nc]))
            heappush(min_heap, [new_diff, nr, nc])


            

if __name__ == "__main__":
    heights = [[1,2,2],[3,8,2],[5,3,5]]
    heights2 = [[1,2,3],[3,8,4],[5,3,5]]
    heights3 = [[1,2,1,1,1],[1,2,1,2,1],[1,2,1,2,1],[1,2,1,2,1],[1,1,1,2,1]]
    print(minimumEffortPath(heights))
