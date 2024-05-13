"""
Given the root of a binary search tree, and an integer k, return the kth smallest value (1-indexed) of all the values of the nodes in the tree.

Example 1:

Input: root = [3,1,4,null,2], k = 1
Output: 1
Example 2:

Input: root = [5,3,6,2,4,null,null,1], k = 3
Output: 3
 
Constraints:

The number of nodes in the tree is n.
1 <= k <= n <= 104
0 <= Node.val <= 104

Follow up: If the BST is modified often (i.e., we can do insert and delete operations) and you need to find the kth smallest frequently, how would you optimize?
"""
def kthSmallest(root, k):
    # if we implement an in_order transversal order we are going to have the list crescent
    # then return k index of that list
    stack = [] 
    def in_order_transversal(root, stack):
        if root:
            in_order_transversal(root.left, stack)
            stack.append(root.val)
            in_order_transversal(root.right, stack)
            
    in_order_transversal(root, stack)
    return stack[k-1] # since the index start em 0