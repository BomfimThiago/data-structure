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
from heapq import heappop, heappush
def kthSmallest(root, k):
    # if we implement an in_order transversal order we are going to have the list crescent
    # then return k index of that list
    heap = []
    def inorder(root):
        if root:
            inorder(root.left)
            heappush(heap, root.val)
            inorder(root.right)

    inorder(root)
    minKVal = 0
    for _ in range(k):
        minKVal = heappop(heap)

    return minKVal


def kthSmallest2(root, k):
    n = 0
    stack = []
    curr = root

    while curr and stack:
        while curr:
            stack.append(curr)
            curr = curr.left

        curr = stack.pop()
        n += 1
        if n == k:
            return curr.val
        
        curr = curr.right

# in a heap I'm sure that I have the min values
# a inorder transversal funcionaria tbm pq ele coloca o esquerdo primeiro e o esquerdo numa bst eh sempre os menores elementos