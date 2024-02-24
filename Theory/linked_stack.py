# # this is a list way of representing a stack
# class Pilha:
#     def __init__(self):
#         self._pilha = []
#         self._size = 0

#     def size(self):
#         return self._size

#     def empty(self):
#         return self._size == 0

#     def peek(self):
#         if self.empty():
#             raise Exception("Pilha vazia")
#         return self._pilha[-1]

#     def push(self, value):
#         self._pilha.append(value)
#         self._size += 1

#     def pop(self):
#         if self.empty():
#             raise Exception("Pilha vazia")
#         self._size -= 1
#         return self._pilha.pop()


# if __name__ == "__main__":
#     pilha = Pilha()
#     for i in range(1, 11):
#         pilha.push(i)
#     print(f"Pilha: {pilha}")

#     for _ in range(1, 6):
#         remove = pilha.pop()
#         print(f"Pop: {remove}")
#     print(f"Pilha: {pilha}")


# # a node way of representing a stack
# class Node:
#     def __init__(self, value):
#         self.value = value
#         self.next = None


# class PilhaNode:
#     def __init__(self):
#         self._topo = Node(None)
#         self._size = 0

#     def size(self):
#         return self._size

#     def is_empty(self):
#         return self._size == 0

#     def push(self, value):
#         new_node = Node(value)
#         new_node.next = self._topo
#         self._topo = new_node

#         self._size += 1

#     def pop(self):
#         if self.is_empty():
#             raise Exception("Pilha vazia")
#         removed = self._topo.value
#         node = self._topo.next
#         self._topo = node

#         if self._size > 0:
#             self._size -= 1

#         return removed

#     def peek(self):
#         if self.is_empty():
#             raise Exception("Pilha vazia")

#         return self._topo.value


# if __name__ == "__main__":
#     pilha = PilhaNode()
#     pilha.push(5)
#     pilha.peek()
#     pilha.push(6)
#     pilha.peek()
#     pilha.pop()
#     pilha.is_empty()
#     pilha.pop()
#     pilha.is_empty()
#     pilha.peek()

# from collections import deque

# if __name__ == "__main__":
#     stack = deque()
#     stack.append(1)
#     stack.extend([2, 3])
#     stack.insert(1, 2)
#     print(len(stack))
#     print(list(stack))
#     stack.pop()

#     queue = deque()
#     queue.append(1)
#     queue.append(2)
#     queue.append(3)
#     queue.popleft()

#     print(list(queue))


class Node:
    def __init__(self, value=None):
        self.value = value
        self.next = None
        self.prev = None


class DoublyLinkedStack:
    def __init__(self):
        self._head = None
        self._tail = None
        self._size = 0

    def size(self):
        return self._size

    def is_empty(self):
        return self._size == 0

    def push_head(self, value):
        new_node = Node(value)

        if not self._tail:
            self._head = new_node
            self._tail = new_node
        else:
            self._head.next = new_node
            new_node.prev = self._head
            self._head = new_node

        self._size += 1

    def push_tail(self, value):
        new_node = Node(value)

        if not self._tail:
            self._head = new_node
            self._tail = new_node
        else:
            new_node.next = self._tail
            self._tail.prev = new_node
            self._tail = new_node

        self._size += 1

    def pop_head(self):
        if self.is_empty():
            raise Exception("Stack is empty")

        removed = self._head.value

        self._head = self._head.prev

        if not self._head:
            self._tail = None
        else:
            self._head.next = None

        if self._size > 0:
            self._size -= 1

        return removed

    # 5 4 3
    def pop_tail(self):
        if self.is_empty():
            raise Exception("Stack is empty")

        removed = self._tail.value

        self._tail = self._tail.next

        if not self._tail:
            self._head = None
        else:
            self._tail.prev = None

        if self._size > 0:
            self._size -= 1

        return removed

    def peek_head(self):
        if self.is_empty():
            raise Exception("Stack is empty")

        return self._head.value

    def peek_tail(self):
        if self.is_empty():
            raise Exception("Stack is empty")

        return self._tail.value
