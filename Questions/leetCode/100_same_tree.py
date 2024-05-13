"""
Given the roots of two binary trees p and q, write a function to check if they are the same or not.

Two binary trees are considered the same if they are structurally identical, and the nodes have the same value.

Example 1:

Input: p = [1,2,3], q = [1,2,3]
Output: true
Example 2:

Input: p = [1,2], q = [1,null,2]
Output: false
Example 3:

Input: p = [1,2,1], q = [1,1,2]
Output: false
"""
class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def isSameTree(p: TreeNode, q: TreeNode):
    if not p and not q:
        return True
    
    if not p or not q or p.val != q.val:
        return False
    
    return (isSameTree(p.left, q.left) and isSameTree(p.right, q.right))


if __name__ == "__main__":
    root = TreeNode(4)
    root.right = TreeNode(7)
    two_node = TreeNode(2)
    
    two_node.left = TreeNode(1)
    two_node.right = TreeNode(3)
    root.left = two_node

    root2 = TreeNode(4)
    root2.right = TreeNode(7)
    two_node_2 = TreeNode(2)
    
    two_node_2.left = TreeNode(1)
    two_node_2.right = TreeNode(3)
    root2.left = two_node_2

    root3 = TreeNode(4)
    root.right = TreeNode(7)
    two_node = TreeNode(2)
    root.left = two_node

    print(isSameTree(root, root2))
    print(isSameTree(root, root3))
    print(isSameTree(root, root))