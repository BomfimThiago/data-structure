"""
Design your implementation of the linked list. You can choose to use a singly or doubly linked list.
A node in a singly linked list should have two attributes: val and next. val is the value of the current node, and next is a pointer/reference to the next node.
If you want to use the doubly linked list, you will need one more attribute prev to indicate the previous node in the linked list. Assume all nodes in the linked list are 0-indexed.

Implement the MyLinkedList class:

MyLinkedList() Initializes the MyLinkedList object.
int get(int index) Get the value of the indexth node in the linked list. If the index is invalid, return -1.
void addAtHead(int val) Add a node of value val before the first element of the linked list. After the insertion, the new node will be the first node of the linked list.
void addAtTail(int val) Append a node of value val as the last element of the linked list.
void addAtIndex(int index, int val) Add a node of value val before the indexth node in the linked list. If index equals the length of the linked list, the node will be appended to the end of the linked list. If index is greater than the length, the node will not be inserted.
void deleteAtIndex(int index) Delete the indexth node in the linked list, if the index is valid.
 

Example 1:

Input
["MyLinkedList", "addAtHead", "addAtTail", "addAtIndex", "get", "deleteAtIndex", "get"]
[[], [1], [3], [1, 2], [1], [1], [1]]
Output
[null, null, null, null, 2, null, 3]

Explanation
MyLinkedList myLinkedList = new MyLinkedList();
myLinkedList.addAtHead(1);
myLinkedList.addAtTail(3);
myLinkedList.addAtIndex(1, 2);    // linked list becomes 1->2->3
myLinkedList.get(1);              // return 2
myLinkedList.deleteAtIndex(1);    // now the linked list is 1->3
myLinkedList.get(1);              // return 3
 

Constraints:

0 <= index, val <= 1000
Please do not use the built-in LinkedList library.
At most 2000 calls will be made to get, addAtHead, addAtTail, addAtIndex and deleteAtIndex.
"""
class ListNode:
    def __init__(self, val):
        self.val = val
        self.next = None

class MyLinkedList:
    def __init__(self):
        self.size = 0
        self.head = None
        self.tail = None

    # tail is the first element
    # head is the last element

    def is_empty(self):
        return self.size == 0

    def get(self, index: int) -> int:
        curr = self.head
        i = 0
        if curr and index == 0:
            return self.tail.val

        while curr and i < (index):
            curr = curr.next
            i += 1

        # if not found
        if not curr and i < (index):
            return -1

        return curr.val
        

    def addAtHead(self, val: int) -> None:
        n = ListNode(val)
        if self.is_empty():
            self.head = n
            self.tail = n
            return
   
        if self.tail == self.head:
            self.tail.next = self.head

        self.head.next = n
        self.head = n
        self.size += 1

    def addAtTail(self, val: int) -> None:
        n = ListNode(val)
        if self.is_empty():
            self.head = n
            self.tail = n
            return

        if self.tail == self.head:
            self.tail.next = self.head

        n.next = self.tail
        self.tail = n
        self.size += 1

    # 0 2 1 2 3 4 5 
    def addAtIndex(self, index: int, val: int) -> None:
        curr = self.head

        if not curr:
            return

        n = ListNode(val)
        if curr and index == 0:
            n.next = self.tail.next
            self.tail = n
            return
        
        i = 0
        # 0 1 2 3 4 
        while curr and i < (index - 1):
            curr = curr.next
            i += 1

        if not curr and i < (index - 1):
            return -1
        
        n.next = curr.next
        curr.next = n
       
     
    def deleteAtIndex(self, index: int) -> None:
        curr = self.head
        if curr and index == 0:
            self.tail = self.tail.next
            return

        i = 0
        while curr and i < (index - 1):
            curr = curr.next
            i += 1
        if not curr and i < (index - 1):
            return

        curr.next = curr.next.next
        return curr.val