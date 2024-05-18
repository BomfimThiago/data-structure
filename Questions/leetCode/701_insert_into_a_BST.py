"""
You are given the root node of a binary search tree (BST) and a value to insert into the tree. Return the root node of the BST after the insertion. It is guaranteed that the new value does not exist in the original BST.

Notice that there may exist multiple valid ways for the insertion, as long as the tree remains a BST after insertion. You can return any of them.

Example 1:


Input: root = [4,2,7,1,3], val = 5
Output: [4,2,7,1,3,5]
Explanation: Another accepted tree is:

Example 2:

Input: root = [40,20,60,10,30,50,70], val = 25
Output: [40,20,60,10,30,50,70,null,null,25]
Example 3:

Input: root = [4,2,7,1,3,null,null,null,null,null,null], val = 5
Output: [4,2,7,1,3,5]
 
"""
class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def insertIntoBST(root, val):
    # BST, small values in the left, greater values in the right
    # return the root node after the insertion
    # is guaranted that the new_node doesnt exist in the tree
    if not root:
        return TreeNode(val)
    if val < root.val:
        root.left = insertIntoBST(root.left, val)
    elif val > root.val:
        root.right = insertIntoBST(root.right, val)

    return


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
    in_order_visit_tree(root)
    insertIntoBST(root, 5)
    in_order_visit_tree(root)
    