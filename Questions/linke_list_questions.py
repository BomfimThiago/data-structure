# Definition for singly-linked list.
class Node:
    def __init__(self, value):
        self.value = value
        self.next = None

# class just to make it easy to see the response
class LinkedList:
    def __init__(self):
        self.start_node = None # first node 
    
    def iterate_list(self):
        print("-----------linked list--------")
        if self.start_node is None:
            print("list has no element")
            return
        else:
            node = self.start_node
            while node is not None:
                print(node.value, "-->")
                node = node.next

# QUESTION 1
"""
There is a singly-linked list head and we want to delete a node node in it.

You are given the node to be deleted node. You will not be given access to the first node of head.

All the values of the linked list are unique, and it is guaranteed that the given node node is not the last node in the linked list.

Delete the given node. Note that by deleting the node, we do not mean removing it from memory. We mean:

The value of the given node should not exist in the linked list.
The number of nodes in the linked list should decrease by one.
All the values before node should be in the same order.
All the values after node should be in the same order.
Custom testing:

For the input, you should provide the entire linked list head and the node to be given node. node should not be the last node of the list and should be an actual node in the list.
We will build the linked list and pass the node to your function.
The output will be the entire list after calling your function.
"""
def deleteNode(head, node):
    """
    :type node: ListNode
    :rtype: void Do not return anything, modify node in-place instead.
    """
    # rules 
    # singly-linked list head, delete node
    # not have access to the first node of head
    # all the values of the linked list is unique
    # the given node is not the lasst node

    # delete node means
    # the value of the given node should not exist in the linkelist head
    # the number of nodes in the linked list should decrease by one
    # all the values before node should be in the same order
    # all the valus after node should be in the same order

    # input the linked list head
    # the node is in the list
    # the output would be the entire list after delete the node
    
    # the current val of the node becomes the next value
    # the current next of the node becomes the next next
    node.value = node.next.value
    node.next = node.next.next

    return head


# QUESTION 2
"""
Given head, the head of a linked list, determine if the linked list has a cycle in it.

There is a cycle in a linked list if there is some node in the list that can be reached again by continuously 
following the next pointer. Internally, pos is used to denote the index of the node that 
tail's next pointer is connected to. Note that pos is not passed as a parameter.

Return true if there is a cycle in the linked list. Otherwise, return false.
"""
def detectLoop(head):
    """
    Floyd’s cycle finding algorithm or Hare-Tortoise algorithm is a pointer algorithm that uses only two pointers, moving through the sequence at different speeds. This algorithm is used to find a loop in a linked list. It uses two pointers one moving twice as fast as the other one. The faster one is called the fast pointer and the other one is called the slow pointer.

    How Does Floyd’s Cycle Finding Algorithm Works?

    While traversing the linked list one of these things will occur-

    The Fast pointer may reach the end (NULL) this shows that there is no loop in the linked list.
    The Fast pointer again catches the slow pointer at some time therefore a loop exists in the linked list.
    """
    n = head.start_node
    if not n or not n.next:
        return False

    slow = n
    fast = n.next
 
    while slow != fast:
        if not fast or not fast.next:
            return False
        
        slow = slow.next
        fast = fast.next.next
    
    return slow.next.value
        
if __name__ == "__main__":
    head = LinkedList()
    n1 = Node(4)
    n2 = Node(5)
    n3 = Node(1)
    n4 = Node(9)

    n1.next = n2
    n2.next = n3
    n3.next = n4
    head.start_node = n1

    head.iterate_list()
    deleteNode(head, n2)
    head.iterate_list()
    

    print(detectLoop(head))
    n5 = Node(10)
    n4.next = n5
    n5.next = n3
    print(detectLoop(head))