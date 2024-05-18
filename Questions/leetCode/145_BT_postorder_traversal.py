"""
Given the root of a binary tree, return the postorder traversal of its nodes' values.
"""
class TreeNode:
    def __init__(self, val=None):
        self.val = val
        self.left = None
        self.right = None

def postorderTraversal(root):
    stack = []
    def helper(root, stack):
        if root:
            helper(root.left, stack)
            helper(root.right, stack)
            stack.append(root.val)
    helper(root, stack)
    return stack


if __name__ == "__main__":
    n1 = TreeNode(10)
    n2 = TreeNode(15)
    n3 = TreeNode(20)
    n1.left = n2
    n1.right = n3
    print(postorderTraversal(n1))