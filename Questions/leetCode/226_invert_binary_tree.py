"""
Given the root of a binary tree, invert the tree, and return its root.

Example 1:

Input: root = [4,2,7,1,3,6,9]
Output: [4,7,2,9,6,3,1]
Example 2:

Input: root = [2,1,3]
Output: [2,3,1]
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

def in_order(root):
    
    if root:
        in_order(root.left)
        print(root.val)
        in_order(root.right)


def invertTree(root):
    if not root:
        return None
    
    root.left, root.right = root.right, root.left
    invertTree(root.right)
    invertTree(root.left)

    return root

if __name__ == "__main__":
    root = TreeNode(4)
    root.right = TreeNode(7)
    two_node = TreeNode(2)
    
    two_node.left = TreeNode(1)
    two_node.right = TreeNode(3)
    root.left = two_node
    print("-------------")
    in_order(root)
    print("-------------")
    new_root = invertTree(root)
    print("-------------")
    in_order(new_root)
    print("-------------")