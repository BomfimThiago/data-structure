"""
Given the root of a binary tree, return the level order traversal of its nodes' values. (i.e., from left to right, level by level).

Input: root = [3,9,20,null,null,15,7]
Output: [[3],[9,20],[15,7]]
Example 2:

Input: root = [1]
Output: [[1]]
Example 3:

Input: root = []
Output: []
"""
from collections import deque
class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def levelOrder(root):
    result = []
    q = deque()

    if root:
        q.append(root)

    while q:
        level = []
        for i in range(len(q)):
            curr = q.popleft()
            level.append(curr.val)

            if curr.left:
                q.append(curr.left)

            if curr.right:
                q.append(curr.right)

        result.append(level)

    return result

if __name__ == "__main__":
    root = TreeNode(4)
    root.right = TreeNode(7)
    two_node = TreeNode(2)
    
    two_node.left = TreeNode(1)
    two_node.right = TreeNode(3)
    root.left = two_node
    print(levelOrder(root))
    
