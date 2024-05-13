"""
Given the roots of two binary trees root and subRoot, return true if there is a subtree of root with the same structure and node values of subRoot and false otherwise.

A subtree of a binary tree tree is a tree that consists of a node in tree and all of this node's descendants. The tree tree could also be considered as a subtree of itself.

Example 1:

Input: root = [3,4,5,1,2], subRoot = [4,1,2]
Output: true
Example 2:

Input: root = [3,4,5,1,2,null,null,null,null,0], subRoot = [4,1,2]
Output: false
"""
class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None

def sameTree(s: TreeNode, t: TreeNode):
    if not s and not t:
        return True

    if s and t and s.val == t.val:
        return sameTree(s.left, t.left) and sameTree(s.right, t.right)
    
    return False

def isSubtree(s: TreeNode, t: TreeNode):
    if not t: return True

    if not s and t: return False

    if sameTree(s, t):
        return True
    else:
        return isSubtree(s.left, t) or isSubtree(s.right, t)