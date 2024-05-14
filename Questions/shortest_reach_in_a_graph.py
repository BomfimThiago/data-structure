"""
Consider an undirected graph consisting of  nodes where each node is labeled from  to  and the edge between any two nodes is always of length . 
We define node  to be the starting position for a BFS. Given a graph, 
determine the distances from the start node to each of its descendants and return the list in node number order, ascending. 
If a node is disconnected, it's distance should be .

For example, there are  nodes in the graph with a starting node . The list of , and each has a weight of .

Starting from node  and creating a list of distances, for nodes  through  we have .

Function Description

Define a Graph class with the required methods to return a list of distances.

Input Format
The first line contains an integer, , the number of queries.

Each of the following  sets of lines is as follows:

The first line contains two space-separated integers,  and , the number of nodes and the number of edges.
Each of the next  lines contains two space-separated integers,  and , describing an edge connecting node  to node .
The last line contains a single integer, , the index of the starting node.
Constraints

Output Format

For each of the  queries, print a single line of  space-separated integers denoting the shortest distances 
to each of the  other nodes from starting position . These distances should be listed sequentially by node number (i.e., ), 
but should not include node . If some node is unreachable from , print  as the distance to that node.
"""
import heapq
from collections import defaultdict, deque
class Graph:
    def __init__(self, n):
        self.n = n
        self.neighbors = defaultdict(set)

    def connect(self, a, b):
        self.neighbors[a].add(b)
        self.neighbors[b].add(a) # undirect

    def find_all_distances(self, start):
        distances = {}
        q = deque((n, 1) for n in self.neighbors[start])
        visited = set([start])

        while q:
            curr_node, dist_from_start = q.popleft()
            if curr_node in visited:
                continue
            visited.add(curr_node)

            distances[curr_node] = dist_from_start * 6
            q.extend((n, dist_from_start + 1) for n in self.neighbors[curr_node])

        for i in range(1, self.n + 1):
            if i == start:
                distances[i] = 0
                continue
            distances[i] = distances.get(i, -1)

        print(distances)
    
if __name__ == "__main__":
    graph = Graph(6)
    edges = [[1,2], [2,3], [3,4], [1, 5]]

    for src, dst in edges:
        graph.connect(src, dst)
        graph.find_all_distances(1)
