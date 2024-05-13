"""
You are given the root of a binary search tree (BST) and an integer val.

Find the node in the BST that the node's value equals val and return the subtree rooted with that node. If such a node does not exist, return null.

Example 1:

Input: root = [4,2,7,1,3], val = 2
Output: [2,1,3]
Example 2:


Input: root = [4,2,7,1,3], val = 5
Output: []
 
"""
class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def searchBST(root: TreeNode, val):
    # it says that its a binary search tree, so in theory its sorted by left and right childreen

    # return the subtree
    # if suche does not exist return null
    if not root:
        return None
    
    if val > root.val:
        return searchBST(root.right, val)
    elif val < root.val:
        return searchBST(root.left, val)
    else:
        return root

def in_order_visit_tree(root):
    if root:
        in_order_visit_tree(root.left)
        print(root.val)
        in_order_visit_tree(root.right)

if __name__ == "__main__":
    root = TreeNode(4)
    root.right = TreeNode(7)
    two_node = TreeNode(2)
    
    two_node.left = TreeNode(1)
    two_node.right = TreeNode(3)
    root.left = two_node
    print(searchBST(root = root, val = 3))
    in_order_visit_tree(root)