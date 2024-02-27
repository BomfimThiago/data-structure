"""
You are given two non-empty linked lists representing two non-negative integers. The digits are stored in reverse order, and each of their nodes contains a single digit. Add the two numbers and return the sum as a linked list.

You may assume the two numbers do not contain any leading zero, except the number 0 itself.

Example 1:
Input: l1 = [2,4,3], l2 = [5,6,4]
Output: [7,0,8]
Explanation: 342 + 465 = 807.
"""
from typing import Optional


class ListNode:
    def __init__(self, value):
        self.value = value
        self.next = None

def addTwoNumbers(l1: Optional[ListNode], l2: Optional[ListNode]):
    dummy = ListNode()
    curr = dummy

    carry = 0 # carry value is the aditional value when we sum something past ten, so adding 6 + 8 we have a 14, 
              # so 4 is my result, my value, and 1 will be my carry
    while l1 or l2 or carry:
        v1 = l1.val if l1 else 0 # we need to remember that the 2 linked list can have differents sizes
        v2 = l2.val if l2 else 0

        # new digit
        val = v1 + v2 + carry
        # if number is above then we have new carry(2 digit number)
        carry = val // 10 # for the carry we want just the divisor
        val = val % 10 # for the value we want the ret (like 14 % 10, my divisor is 1 and my rest is 4)

        curr.next = ListNode(val)

        # update pointers
        cur = cur.next
        l1 = l1.next if l1 else None
        l2 = l2.next if l2 else None

    return dummy.next