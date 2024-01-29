# this is a list way of representing a stack
class Pilha:
    def __init__(self):
        self._pilha = []
        self._size = 0

    def size(self):
        return self._size

    def empty(self):
        return self._size == 0

    def peek(self):
        if self.empty():
            raise Exception("Pilha vazia")
        return self._pilha[-1]

    def push(self, value):
        self._pilha.append(value)
        self._size += 1

    def pop(self):
        if self.empty():
            raise Exception("Pilha vazia")
        self._size -= 1
        return self._pilha.pop()


if __name__ == "__main__":
    pilha = Pilha()
    for i in range(1, 11):
        pilha.push(i)
    print(f"Pilha: {pilha}")

    for _ in range(1, 6):
        remove = pilha.pop()
        print(f"Pop: {remove}")
    print(f"Pilha: {pilha}")


# a node way of representing a stack
class Node:
    def __init__(self, value):
        self.value = value
        self.next = None


class PilhaNode:
    def __init__(self):
        self._topo = Node(None)
        self._size = 0

    def size(self):
        return self._size

    def is_empty(self):
        return self._size == 0

    def push(self, value):
        new_node = Node(value)
        new_node.next = self._topo
        self._topo = new_node

        self._size += 1

    def pop(self):
        if self.is_empty():
            raise Exception("Pilha vazia")
        removed = self._topo.value
        node = self._topo.next
        self._topo = node

        if self._size > 0:
            self._size -= 1

        return removed

    def peek(self):
        if self.is_empty():
            raise Exception("Pilha vazia")

        return self._topo.value


if __name__ == "__main__":
    pilha = PilhaNode()
    pilha.push(5)
    pilha.peek()
    pilha.push(6)
    pilha.peek()
    pilha.pop()
    pilha.is_empty()
    pilha.pop()
    pilha.is_empty()
    pilha.peek()
