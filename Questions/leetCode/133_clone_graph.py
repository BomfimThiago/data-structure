"""
Given a reference of a node in a connected undirected graph.

Return a deep copy (clone) of the graph.

Each node in the graph contains a value (int) and a list (List[Node]) of its neighbors.

class Node {
    public int val;
    public List<Node> neighbors;
}
 

Test case format:

For simplicity, each node's value is the same as the node's index (1-indexed). 
For example, the first node with val == 1, the second node with val == 2, and so on. 
The graph is represented in the test case using an adjacency list.

An adjacency list is a collection of unordered lists used to represent a finite graph. 
Each list describes the set of neighbors of a node in the graph.

The given node will always be the first node with val = 1. 
You must return the copy of the given node as a reference to the cloned graph.
"""
from collections import defaultdict
class Node:
    def __init__(self, val):
        self.val = val
        self.neighbours = []

def cloneGraph(adj):
    d = defaultdict(list)
    for o, dest in adj:
        d[o].append(dest)

    nodes = []
    for key, val in d.items():
        n = Node(key)
        n.neighbours.extend(val)
        nodes.append(n)
    
    print(nodes)

if __name__ == "__main__":
    print(cloneGraph(adj = [[1,4],[1,3],[2,4],[2,3]]))