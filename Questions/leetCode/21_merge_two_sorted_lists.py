"""
You are given the heads of two sorted linked lists list1 and list2.

Merge the two lists into one sorted list. The list should be made by splicing together the nodes of the first two lists.

Return the head of the merged linked list.

Example 1:

Input: list1 = [1,2,4], list2 = [1,3,4]
Output: [1,1,2,3,4,4]
Example 2:

Input: list1 = [], list2 = []
Output: []
Example 3:

Input: list1 = [], list2 = [0]
Output: [0]
 
Constraints:

The number of nodes in both lists is in the range [0, 50].
-100 <= Node.val <= 100
Both list1 and list2 are sorted in non-decreasing order.
"""
from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


def mergeTwoLists(list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
    n1 = list1
    n2 = list2

    newNode = ListNode(None)
    dummy = newNode

    while n1 and n2:
        if n1.val <= n2.val:
            newNode.next = n1 
            n1 = n1.next
        else:
            newNode.next = n2
            n2 = n2.next
        newNode = newNode.next
    if n1:
        newNode.next = n1
    if n2:
        newNode.next = n2

    return dummy.next