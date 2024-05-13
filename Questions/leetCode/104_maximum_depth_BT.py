"""
104. Maximum Depth of Binary Tree
Easy
Topics
Companies
Given the root of a binary tree, return its maximum depth.

A binary tree's maximum depth is the number of nodes along the longest path from the root node down to the farthest leaf node.

Example 1:

Input: root = [3,9,20,null,null,15,7]
Output: 3
Example 2:

Input: root = [1,null,2]
Output: 2
"""
class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

from collections import deque
# this bfs(breadth first search)
def maxDepth(root):
    # visit by levels and count the level
    q = deque()
    if root:
        q.append(root)
    maxD = 0
    while q:
        for i in range(len(q)):
            curr = q.popleft()

            if curr.left:
                q.append(curr.left)
            if curr.right:
                q.append(curr.right)
        maxD += 1

    return maxD
# this is dfs
def maxDepth2(root):
    if not root:
        return 0
    
    return 1 + max(maxDepth2(root.left), maxDepth2(root.right))

if __name__ == "__main__":
    root = TreeNode(4)
    root.right = TreeNode(7)
    two_node = TreeNode(2)
    
    two_node.left = TreeNode(1)
    two_node.right = TreeNode(3)
    root.left = two_node
    print(maxDepth(root))
    print(maxDepth2(root))