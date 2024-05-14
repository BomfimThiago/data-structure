"""
You are given an undirected weighted graph of n nodes (0-indexed), represented by an edge list where edges[i] = [a, b] is an undirected edge connecting the nodes a and b with a probability of success of traversing that edge succProb[i].

Given two nodes start and end, find the path with the maximum probability of success to go from start to end and return its success probability.

If there is no path from start to end, return 0. Your answer will be accepted if it differs from the correct answer by at most 1e-5.

Input: n = 3, edges = [[0,1],[1,2],[0,2]], succProb = [0.5,0.5,0.2], start = 0, end = 2
Output: 0.25000
Explanation: There are two paths from start to end, one having a probability of success = 0.2 and the other has 0.5 * 0.5 = 0.25.
Example 2:

Input: n = 3, edges = [[0,1],[1,2],[0,2]], succProb = [0.5,0.5,0.3], start = 0, end = 2
Output: 0.30000
Example 3:

Input: n = 3, edges = [[0,1]], succProb = [0.5], start = 0, end = 2
Output: 0.00000
Explanation: There is no path between 0 and 2.
"""
import heapq
from collections import defaultdict
def maxProbability(n, edges, succProb, start, end):
    # undirected(can go and back)
    # n number of nodes
    # edfes[i] = [a, b] with a probability of succes of transversing that edge succProb[i]
    # ex.  edges = [[0,1],[1,2],[0,2]], succProb = [0.5,0.5,0.2], to go from 0 to 1 the prob is 0.5, 1 to 2 the prob is 0.5 and 
    # to go from 0 to 2 the probability is 0.2
    # to go from start_node to end_node find the path with maxProbability
    # if there is no path from start, end return 0

    # okay maybe use the heap but with the maximum? if I'm not mistake we need to multiply by -1 in python 

    # first mount the adjacency list
    adj = defaultdict(list)
    for i in range(n):
        src, dst = edges[i]
        # we do this twice because the nodes are undirected
        adj[src].append([dst, succProb[i]]) 
        adj[dst].append([src, succProb[i]])


    
    maxHeap = [(-1, start)]
    visit = set()

    while maxHeap:
        prob, n1 = heapq.heappop(maxHeap)
        if n1 in visit:
            continue

        if n1 == end:
            return prob * -1 # we are dealing with max heap

        for n2, prob2 in adj[n1]:
            if n2 not in visit:
                heapq.heappush(maxHeap, (prob + prob2, n2))


if __name__ == "__main__":
    print(maxProbability(n = 3, edges = [[0,1],[1,2],[0,2]], succProb = [0.5,0.5,0.2], start = 0, end = 2))