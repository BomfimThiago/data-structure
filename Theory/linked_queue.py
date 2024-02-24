# # FIFO first in first out
# class Node:
#     def __init__(self, value):
#         self.value = value
#         self.next = None


# # methods size, peek, pop, push, is_empty
# class Fila:
#     def __init__(self):
#         self._top = None  # first node
#         self._end = None
#         self._size = 0

#     def size(self):
#         return self._size

#     def is_empty(self):
#         return self._size == 0

#     def push(self, value):
#         new_node = Node(value)
#         if self._end is None:
#             self._top = new_node
#             self._end = new_node
#         else:
#             self._end.next = new_node
#             self._end = new_node
#         self._size += 1

#     def pop(self):
#         if self.is_empty():
#             raise Exception("Fila vazia")
#         removed = self._top.value
#         self._top = self._top.next
#         if self._top is None:
#             self._end = None

#         if self._size > 0:
#             self._size -= 1
#         return removed

#     def peek_top(self):
#         if self.is_empty():
#             raise Exception("Fila vazia")
#         return self._top.value

#     def peek_fim(self):
#         if self.is_empty():
#             raise Exception("Fila vazia")
#         return self._end.value


# if __name__ == "__main__":
#     fila = Fila()

#     fila.push(1)
#     fila.peek_first()
#     fila.peek_top()

#     fila.push(2)
#     fila.peek_first()
#     fila.peek_top()

#     fila.push(3)
#     fila.peek_first()
#     fila.peek_top()

#     fila.pop()
#     fila.peek_first()
#     fila.peek_top()

#     fila.pop()
#     fila.peek_first()
#     fila.peek_top()


# class Node:
#     def __init__(self, value):
#         self.value = value
#         self.next = None


# # 6 methods, peek_first(), peek_last(), size(), is_empty(), push(), pop()
# class Queue:
#     def __init__(self):
#         self._top = None
#         self._end = None
#         self._size = 0

#     def size(self):
#         return self._size

#     def is_empty(self):
#         return self._size == 0

#     def push(self, value):
#         new_node = Node(value)

#         if not self._end:
#             self._top = new_node
#             self._end = new_node
#         else:
#             self._end.next = new_node
#             self._end = new_node

#         self._size += 1

#     def pop(self):
#         if self.is_empty():
#             raise Exception("Queue is empty")

#         removed = self._top.value

#         self._top = self._top.next
#         if not self._top:
#             self._end = None

#         if self._size > 0:
#             self._size -= 1

#         return removed

#     def peek_top(self):
#         if self.is_empty():
#             raise Exception("Queue is empty")

#         return self._top.value

#     def peek_end(self):
#         if self.is_empty():
#             raise Exception("Queue is empty")

#         return self._end.value


class Node:
    def __init__(self, value=None, next=None, prev=None):
        self.value = value
        self.next = next
        self.prev = prev


class DoublyLinkedQueue:
    def __init__(self):
        self._head = None
        self._tail = None
        self._size = 0

    def size(self):
        return self._size

    def is_empty(self):
        return self._size == 0

    def push_tail(self, value):
        new_node = Node(value)

        if not self._tail:
            self._head = new_node
            self._tail = new_node
        else:
            self._tail.next = new_node
            new_node.prev = self._tail
            self._tail = new_node
        self._size += 1

    def push_head(self, value):
        new_node = Node(value)

        if not self._tail:
            self._head = new_node
            self._tail = new_node
        else:
            new_node.next = self._head
            self._head.prev = new_node
            self._head = new_node

        self._size += 1

    def pop_head(self):
        if self.is_empty():
            raise Exception("Doubly Linked Queue is empty")

        removed = self._head.value

        self._head = self._head.next

        if not self._head:
            self._tail = None
        else:
            self._head.prev = None

        if self._size > 0:
            self._size -= 1

        return removed

    def pop_tail(self):
        if self.is_empty():
            raise Exception("Doubly Linked Queue is empty")

        removed = self._tail.value

        self._tail = self._tail.prev

        if self._tail:
            self._tail.next = None
        else:
            self._head = None

        if self._size > 0:
            self._size -= 1

        return removed

    def peek_head(self):
        if self.is_empty():
            raise Exception("Doubly Linked Queue is empty")
        return self._head.value

    def peek_tail(self):
        if self.is_empty():
            raise Exception("Doubly Linked Queue is empty")
        return self._tail.value
