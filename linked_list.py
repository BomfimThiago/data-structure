"""
A single linked list is the simplest of all the variants of linked lists. 
Every node in a single linked list contains an item and a reference to the next item and that's it. 
In this section, we will see how to create a node for the single linked list along with the methods 
for different types of insertion, traversal, and deletion.
"""

class Node:
    def __init__(self, value):
        self.value = value
        self.next = None

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

   
    # inserting in the beggining is the easiest way of inserting
    def insert_at_start(self, value):
        new_node = Node(value)
        new_node.next = self.start_node
        self.start_node = new_node

    def insert_at_end(self, value):
        new_node = Node(value)
        if self.start_node is None:
            self.start_node = new_node
            return

        node = self.start_node
        while node.next is not None:
            # we iterate until reach the last node
            node = node.next

        # then we say that the next of the last node is the new_node
        node.next = new_node

    def insert_node_after_another_node(self, another_node, value):
        new_node = Node(value)
        node = self.start_node
        # first look for the node
        while node is not None:
            if node.value == another_node.value and node.next == another_node.next:
                break
            node = node.next

        if node is None:
            print("node is not in the list")
        else:
            new_node.next = node.next
            node.next = new_node

    def insert_node_before_another_node(self, another_node, value):
        new_node = Node(value)
        node = self.start_node

        # find the node before another node
        while node.next is not None:
            if node.next.value == another_node.value and node.next.next == another_node.next:
                break

            node = node.next

        if node is None:
            print("node is not in the list")
        else:
            new_node.next = node.next
            node.next = new_node

    def insert_in_specific_index(self, index, value):
        new_node = Node(value)
        node = self.start_node
        before_node = None
        count_index = 0

        if index == 0 and self.start_node is not None:
            new_node.next = self.start_node.next
            self.start_node = new_node
            return

        while node is not None:
            if count_index == index:
                break
            count_index += 1
            before_node = node
            node = node.next

        if node is None:
            print("index out of range")
        else:
            before_node.next = new_node
            new_node.next = node

    def count(self):
        if not self.start_node:
            return 0
        
        if not self.start_node.next:
            return 1
        
        count = 0
        node = self.start_node
        while node is not None:
            count += 1
            node = node.next

        return count
    
    def search_item(self, x):
        if self.start_node is None:
            print("List has no elements")
            return
        n = self.start_node
        while n is not None:
            if n.value == x:
                print("Item found")
                return True
            n = n.next
        print("item not found")
        return False


    def delete_first_node(self):
        if not self.start_node:
            print("node has not element")
            return

        if not self.start_node.next:
            self.start_node = None
            return

        node = self.start_node
        self.start_node = node.next

    def delete_last_node(self):
        if not self.start_node:
            print("node has not element")
            return

        if not self.start_node.next:
            self.start_node = None
            return
        
        node = self.start_node
        while node.next.next is not None:
            # n3.next is None
            # n3 is the last
            # n2.next needs to be none
            # n2.next is equal to n3, n2.next.next is none because n3 is the last element
            node = node.next

        # we find n2
        node.next = None


    def delete_node(self, node):
        if not self.start_node:
            print("list has no node")
            return
        
        # search for the node
        n = self.start_node
        while n.next is not None:
            if n.next.value == node.value and n.next.next == node.next:
                # we found the previous node before the node we want to delete
                break
            n = n.next

        if n is None:
            print("node is not in the list")
        else:
            # n1 n2 n3
            n.next = node.next


    def reverse_linkedlist(self):
        prev = None
        node = self.start_node

        if self.start_node.next is None:
            return

        while node is not None:
            # revert is make the node point to the prev node
            next = node.next # n2
            node.next = prev # none
            prev = node # n1
            node = next # n2
        self.start_node = prev # prev here will be the last element
        



if __name__ == '__main__':
    n1 = Node(10)
    n2 = Node(2)
    n3 = Node(4)
    n4 = Node(5)
    n5 = Node(6)
    n6 = Node(8)
    n7 = Node(14)

    n1.next = n2
    n2.next = n3
    n3.next = n4
    n4.next = n5
    n5.next = n6
    n6.next = n7

    # linkedList = LinkedList()
    # linkedList.start_node = n1

    # linkedList.iterate_list()

    # linkedList.insert_at_start(15)

    # linkedList.iterate_list()

    # linkedList.insert_at_end(20)
    # linkedList.iterate_list()

    # linkedList.insert_node_after_another_node(n2, 35)
    # linkedList.iterate_list()
    # linkedList.insert_node_after_another_node(n4, 10)

    # linkedList.insert_node_before_another_node(n2,13)
    # linkedList.iterate_list()
    # linkedList.insert_node_before_another_node(n4, 10)

    # linkedList.insert_in_specific_index(1, 3)
    # linkedList.iterate_list()
    # linkedList.insert_in_specific_index(20, 9)
    # linkedList.insert_in_specific_index(0, 9)
    # linkedList.iterate_list()

    # print("---- count -----", linkedList.count())

    # l2 = LinkedList()
    # print("---- count2 -----", l2.count())
    # l2.start_node = n1
    # print("---- count2 -----", l2.count())
    # l2.iterate_list()

    l3 = LinkedList()
    l3.start_node = n1
    l3.iterate_list()

    l3.search_item(4)
    l3.search_item(15)

    print("deleting first item")
    l3.delete_first_node()
    l3.iterate_list()
    print("---- count3 -----", l3.count())

    print("deleting last item")
    l3.delete_last_node()
    l3.iterate_list()
    print("---- count3 -----", l3.count())

    print("deleting node3(4)")
    l3.delete_node(n3)
    l3.iterate_list()
    print("---- count3 -----", l3.count())

    l3.iterate_list()
    l3.reverse_linkedlist()
    l3.iterate_list()