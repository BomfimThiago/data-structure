"""
The thief has found himself a new place for his thievery again. There is only one entrance to this area, called root.

Besides the root, each house has one and only one parent house. After a tour, the smart thief realized 
that all houses in this place form a binary tree. It will automatically contact the police if two directly-linked houses were broken into on the same night.

Given the root of the binary tree, return the maximum amount of money the thief can rob without alerting the police.

Input: root = [3,4,5,1,3,null,1]
Output: 9
Explanation: Maximum amount of money the thief can rob = 4 + 5 = 9.
"""
class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None

def rob(root):
    def dfs(root, cache):
        if not root:
            return 0
        
        if root in cache:
            return cache[root]
        
        countLeft = 0
        if root.left:
            countLeft = dfs(root.left.left, cache) + dfs(root.left.right, cache)
        countRight = 0
        if root.right:
            countRight = dfs(root.right.left, cache) + dfs(root.right.right, cache)
        
        cache[root] = max(
            root.val +  countLeft + countRight,
            dfs(root.left, cache) + dfs(root.right, cache)
        )

        return cache[root]
    return dfs(root, {})

if __name__ == "__main__":
    root = TreeNode(3)
    n1 = TreeNode(4)
    n2 = TreeNode(5)
    n3 = TreeNode(1)
    n4 = TreeNode(3)
    n5 = TreeNode(1)
    root.left = n1
    n1.left = n3
    n1.right = n4
    root.right = n2
    n2.right = n5
    n2.left = None
    
    print(rob(root))