"""
Given the head of a singly linked list, return true if it is a 
palindrome
 or false otherwise.

Example 1:

Input: head = [1,2,2,1]
Output: true
Example 2:

Input: head = [1,2]
Output: false
"""
class Node:
    def __init__(self, val):
        self.val = val
        self.next = None

# Time Complexity O(n) and space O(1)
def isPalindrome(head: Node):
    nums = []
    curr = head
    while curr:
        nums.append(curr.val)
        curr = curr.next

    # is Palindrome
    l = 0
    r = len(nums) - 1
    while l <= r:
        if nums[l] != nums[r]:
            return False
        l += 1
        r -= 1
    return True

def isPalindrome2(head: Node):
    # fast and slow pointer, and then reverse the middle
    # and then we can check if they are equal(for me its kind of pointless)
    slow, fast = head, head
    # find middle
    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next

    # reverse second half
    prev = None
    next_node = None
    while slow:
        next_node = slow.next
        slow.next = prev
        prev = slow
        slow = next_node

    # compare prev with the head
    while prev:
        if prev.val != head.val:
            return False
        prev = prev.next
        head = head.next

    return True
    
if __name__ == "__main__":
    n1 = Node(1)
    n2 = Node(2)
    n3 = Node(3)
    n4 = Node(4)
    n5 = Node(3)
    n6 = Node(2)
    n7 = Node(1)

    n1.next = n2
    n2.next = n3
    n3.next = n4
    n4.next = n5
    n5.next = n6
    n6.next = n7

    n8 = Node(1)
    n9 = Node(2)
    n10 = Node(2)
    n11 = Node(1)

    n8.next = n9
    n9.next = n10
    n10.next = n11

    print(isPalindrome(n8))