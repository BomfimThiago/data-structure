"""
Adjancency List DFS
Question:
Count the number of paths that lead from a source to destination
adjList = {"A": ["B"], "B": ["C", "E"], "C": ["E"], "D": [], "E": ["D"]}
"""
def dfs(node, target, adjList, visit):
    if node in visit:
        return 0
    if node == target:
        return 1
    
    count = 0
    visit.add(node)

    for neighbour in adjList.get(node, []):
        count += dfs(neighbour, target, adjList, visit)

    visit.remove(node)
    return count

if __name__ == "__main__":
    adjList = {"A": ["B"], "B": ["C", "E"], "C": ["E"], "D": [], "E": ["D"]}
    print("dfs in adjancecy list----")
    print(dfs("A", "E", adjList, set()))

"""
Adjancency List BFS 
Question:
Find the shortest path from node to target, we reach the destination visiting fewest vertices possible
adjList = {"A": ["B"], "B": ["C", "E"], "C": ["E"], "D": [], "E": ["D"]}
"""
from collections import deque

def bfs(adjList):
    target = "E"
    visit = set()
    queue = deque()
    queue.append("A")
    visit.add("A")

    count = 0
    while queue:
        for i in range(len(queue)):
            node = queue.popleft()

            if node == target:
                return count

            neighbours = adjList.get(node, [])
            for n in neighbours:
                if n in visit:
                    return 0
                queue.append(n)
                visit.add(n)
        count += 1
                
        
    
if __name__ == "__main__":
    adjList = {"A": ["B"], "B": ["C"], "C": ["F"], "D": [], "E": ["D"], "F": "E"}
    print("bfs in adjancecy list----")
    print(bfs(adjList))