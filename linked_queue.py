# FIFO first in first out
class Node:
    def __init__(self, value):
        self.value = value
        self.next = None


# methods size, peek, pop, push, is_empty
class Fila:
    def __init__(self):
        self._top = None  # first node
        self._end = None
        self._size = 0

    def size(self):
        return self._size

    def is_empty(self):
        return self._size == 0

    def push(self, value):
        new_node = Node(value)
        if self._end is None:
            self._top = new_node
            self._end = new_node
        else:
            self._end.next = new_node
            self._end = new_node
        self._size += 1

    def pop(self):
        if self.is_empty():
            raise Exception("Fila vazia")
        removed = self._top.value
        self._top = self._top.next
        if self._top is None:
            self._end = None

        if self._size > 0:
            self._size -= 1
        return removed

    def peek_top(self):
        if self.is_empty():
            raise Exception("Fila vazia")
        return self._top.value

    def peek_fim(self):
        if self.is_empty():
            raise Exception("Fila vazia")
        return self._end.value


if __name__ == "__main__":
    fila = Fila()

    fila.push(1)
    fila.peek_first()
    fila.peek_top()

    fila.push(2)
    fila.peek_first()
    fila.peek_top()

    fila.push(3)
    fila.peek_first()
    fila.peek_top()

    fila.pop()
    fila.peek_first()
    fila.peek_top()

    fila.pop()
    fila.peek_first()
    fila.peek_top()
