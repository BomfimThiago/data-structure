"""
Given the root of a binary tree, imagine yourself standing on the right side of it, return the values 
of the nodes you can see ordered from top to bottom.

Example 1:

Input: root = [1,2,3,null,5,null,4]
Output: [1,3,4]
Example 2:

Input: root = [1,null,3]
Output: [1,3]
Example 3:

Input: root = []
Output: []
 
Constraints:

The number of nodes in the tree is in the range [0, 100].
-100 <= Node.val <= 100
"""

from collections import deque
class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None

def rightSideView(root):
    result = []
   
    q = deque()
    if root:
        q.append(root)

    while len(q) > 0:
        level = []
        for i in range(len(q)):
            curr = q.popleft()
            level.append(curr.val)
            if curr.left:
                q.append(curr.left)

            if curr.right:
                q.append(curr.right)

        result.append(level[-1])

    return result

if __name__ == "__main__":
    root = TreeNode(4)
    root.right = TreeNode(7)
    two_node = TreeNode(2)
    
    two_node.left = TreeNode(1)
    two_node.right = TreeNode(3)
    root.left = two_node
    print(rightSideView(root))