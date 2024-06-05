"""
Given an undirected tree consisting of n vertices numbered from 0 to n-1, which has some apples in their vertices. 
You spend 1 second to walk over one edge of the tree. Return the minimum time in seconds you have to spend to collect all apples in the tree, starting at vertex 0 and coming back to this vertex.

The edges of the undirected tree are given in the array edges, where edges[i] = [ai, bi] 
means that exists an edge connecting the vertices ai and bi. Additionally, 
there is a boolean array hasApple, where hasApple[i] = true means that vertex i has an apple; otherwise, 
it does not have any apple.


Input: n = 7, edges = [[0,1],[0,2],[1,4],[1,5],[2,3],[2,6]], hasApple = [false,false,true,false,true,true,false]
Output: 8 
Explanation: The figure above represents the given tree where red vertices have an apple. 
One optimal path to collect all apples is shown by the green arrows.  

Input: n = 7, edges = [[0,1],[0,2],[1,4],[1,5],[2,3],[2,6]], hasApple = [false,false,true,false,false,true,false]
Output: 6
Explanation: The figure above represents the given tree where red vertices have an apple. 
One optimal path to collect all apples is shown by the green arrows.  


Input: n = 7, edges = [[0,1],[0,2],[1,4],[1,5],[2,3],[2,6]], 
hasApple = [false,false,false,false,false,false,false]
Output: 0
 
"""
from collections import defaultdict
class TreeNode:
    def __init__(self, val=None):
        self.val = val
        self.left = None
        self.right = None

def minTime(n, edges, hasApple):
    adj = {i: [] for i in range(n)}

    for par, child in edges:
        adj[par].append(child)
        adj[child].append(par)

    def dfs(curr, par):
        time = 0
        for child in adj[curr]:
            if child == par:
                continue
            childTime = dfs(child, curr)
            if childTime or hasApple[child]:
                time += 2 + childTime
        return time
    return dfs(0, -1)


if __name__ == "__main__":
    n = 7
    edges = [[0,1],[0,2],[1,4],[1,5],[2,3],[2,6]]
    hasApple = [False,False,True,False,True,True,False]
    print(minTime(n, edges, hasApple))