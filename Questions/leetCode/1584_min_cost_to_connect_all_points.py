"""
You are given an array points representing integer coordinates of some points on a 2D-plane, where points[i] = [xi, yi].

The cost of connecting two points [xi, yi] and [xj, yj] is the manhattan distance between them: |xi - xj| + |yi - yj|, where |val| denotes the absolute value of val.

Return the minimum cost to make all points connected. All points are connected if there is exactly one simple path between any two points.
"""
from heapq import heappop, heappush
def minCostConnectPoints(points):
    N = len(points)

    # basically build all connections between the nodes
    adj = {i: [] for i in range(N)}
    for i in range(N):
        x1, y1 = points[i]
        for j in range(i + 1, N):
            x2, y2 = points[j]
            dist = abs(x1 - x2) + abs(y1 - y2)
            adj[i].append([dist, j])
            adj[j].append([dist, i])

    # Prims alhorithm
    res = 0
    visited = set()
    min_heap = [[0, 0]]
    while len(visited) < N:
        cost, i = heappop(min_heap)
        if i in visited:
            continue
        res += cost
        visited.add(i)
        for nei_cost, nei in adj[i]:
            if nei not in visited:
                heappush(min_heap, [nei_cost, nei])

    return res


if __name__ == "__main__":
    points = [[0,0],[2,2],[3,10],[5,2],[7,0]] # output 20
    print(minCostConnectPoints(points))
