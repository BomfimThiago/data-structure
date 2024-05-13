"""
Given a root node reference of a BST and a key, delete the node with the given key in the BST. Return the root node reference (possibly updated) of the BST.

Basically, the deletion can be divided into two stages:

Search for a node to remove.
If the node is found, delete the node.
 
Example 1:

Input: root = [5,3,6,2,4,null,7], key = 3
Output: [5,4,6,2,null,null,7]
Explanation: Given key to delete is 3. So we find the node with value 3 and delete it.
One valid answer is [5,4,6,2,null,null,7], shown in the above BST.
Please notice that another valid answer is [5,2,6,null,4,null,7] and it's also accepted.

Example 2:

Input: root = [5,3,6,2,4,null,7], key = 0
Output: [5,3,6,2,4,null,7]
Explanation: The tree does not contain a node with value = 0.
Example 3:

Input: root = [], key = 0
Output: []

"""
class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def in_order_visit_tree(root):
    if root:
        in_order_visit_tree(root.left)
        print(root.val)
        in_order_visit_tree(root.right)

def min_value(root):
    curr = root
    while curr and curr.left:
        curr = curr.left

    return curr

def deleteNode(root, val):
    if not root:
        return None
    
    if val > root.val:
        root.right = deleteNode(root.right, val)
    elif val < root.val:
        root.left = deleteNode(root.left, val)
    else:
        if not root.right:
            return root.left
        elif not root.left:
            return root.right
        else:
            minNode = min_value(root.right)
            root.val = minNode.val
            root.right = deleteNode(root.right, minNode.val)

    return root

if __name__ == "__main__":
    root = TreeNode(4)
    root.right = TreeNode(7)
    two_node = TreeNode(2)
    
    two_node.left = TreeNode(1)
    two_node.right = TreeNode(3)
    root.left = two_node
    print(deleteNode(root = root, val = 2))
    in_order_visit_tree(root)