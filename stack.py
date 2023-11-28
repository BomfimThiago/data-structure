"""
Last-In/First-Out(LIFO) or 
Firs-In/Last-Out

In stack, a new element is added at one end and an element is removed from that end only
insert and delete operations are often called push and pop

The functions associated with stack are:

empty() - Returns whether the stack is empty - Time Complexity: O(1)
size() - Returns the size of the stack - Time Complexity: O(1)
top() / peek() - Returns a reference to the topmost element of the stack - Time Complexity: O(1)
push(a) - Inserts the element ‘a’ at the top of the stack - Time Complexity: O(1)
pop() - Deletes the topmost element of the stack - Time Complexity: O(1)


In python we can implement stacks following 3 ways
- list
- Collections.deque
Deque (Doubly Ended Queue) in Python is implemented using the module “collections“. 
Deque is preferred over a list in the cases where we need quicker append and pop operations 
from both the ends of the container, as deque provides an O(1) time complexity 
for append and pop operations as compared to a list that provides O(n) time complexity.
- queue.LifoQueue
"""

# implementation using list
# is not as efficient, including an element in the beggining or in the middle of the stack has time complexity O(n)
stack = []
stack.append('a') # first in, if we do a pop it will be the last out
stack.append('b')
stack.append('c') # last in, if we do a pop it will be the first out

print('\nElements popped from stack:')
print(stack.pop())
print(stack.pop())
print(stack.pop())
 
print('\nStack after elements are popped:')
print(stack)

# implementation using collections.deque
from collections import deque

stack =  deque()

# append() function to push
# element in the stack
stack.append('a')
stack.append('b')
stack.append('c')
 
print('Initial stack:')
print(stack)
 
# pop() function to pop
# element from stack in
# LIFO order
print('\nElements popped from stack:')
print(stack.pop())
print(stack.pop())
print(stack.pop())
 
print('\nStack after elements are popped:')
print(stack)

# its ease to add or remove element of the beggining or the middle of the stack
stack.append('a')
stack.append('b')
stack.append('c')
stack.appendleft('d') # append in the beggining of stack
stack.insert(3, 'e') # insert in the middle of the stack
print(stack)

stack.popleft() # remove the first element
print(stack)


"""
extend(iterable):- This function is used to add multiple values at the right end of the deque. 
The argument passed is iterable.

extendleft(iterable):- This function is used to add multiple values at the left end of the deque.
The argument passed is iterable. Order is reversed as a result of left appends.

reverse():- This function is used to reverse the order of deque elements.

rotate():- This function rotates the deque by the number specified in arguments. 
If the number specified is negative, rotation occurs to the left. Else rotation is to right.
"""
"""
summary: 

from collections import deque
d = deque('ghi')                 # make a new deque with three items
for elem in d:                   # iterate over the deque's elements
    print(elem.upper())

d.append('j')                    # add a new entry to the right side
d.appendleft('f')                # add a new entry to the left side

d.pop()                          # return and remove the rightmost item

d.popleft()                      # return and remove the leftmost item

list(d)                          # list the contents of the deque

d[0]                             # peek at leftmost item

d[-1]                            # peek at rightmost item

list(reversed(d))                # list the contents of a deque in reverse

'h' in d                         # search the deque

d.extend('jkl')                  # add multiple elements at once

d.rotate(1)                      # right rotation

d.rotate(-1)                     # left rotation

deque(reversed(d))               # make a new deque in reverse order

d.clear()                        # empty the deque

d.pop()                          # cannot pop from an empty deque

d.extendleft('abc')              # extendleft() reverses the input order

"""

# implementing using Queue
"""
Queue module also has a LIFO Queue, which is basically a Stack. Data is inserted into Queue using the put() function and get() takes data out from the Queue. 

There are various functions available in this module: 

maxsize – Number of items allowed in the queue.
empty() – Return True if the queue is empty, False otherwise.
full() – Return True if there are maxsize items in the queue. If the queue was initialized with maxsize=0 (the default), then full() never returns True.
get() – Remove and return an item from the queue. If the queue is empty, wait until an item is available.
get_nowait() – Return an item if one is immediately available, else raise QueueEmpty.
put(item) – Put an item into the queue. If the queue is full, wait until a free slot is available before adding the item.
put_nowait(item) – Put an item into the queue without blocking. If no free slot is immediately available, raise QueueFull.
qsize() – Return the number of items in the queue.
"""



# Python program to
# demonstrate stack implementation
# using queue module
 
from queue import LifoQueue
 
# Initializing a stack
stack = LifoQueue(maxsize=3)
 
# qsize() show the number of elements
# in the stack
print(stack.qsize())
 
# put() function to push
# element in the stack
stack.put('a')
stack.put('b')
stack.put('c')
 
print("Full: ", stack.full())
print("Size: ", stack.qsize())
 
# get() function to pop
# element from stack in
# LIFO order
print('\nElements popped from the stack')
print(stack.get())
print(stack.get())
print(stack.get())
 
print("\nEmpty: ", stack.empty())

# implement a stack with linked list
class Node:
    def __init__(self, value):
        self.value = value
        self.next = None

class Stack:
    def __init__(self):
        self.head = Node("head")
        self._size = 0

    def __str__(self):
        current = self.head.next
        out = ""
        while current:
            out += str(current.value) + "->"
            current = current.next
        
        return out[:-2]
    
    def size(self):
        return self._size
    
    def is_empty(self):
        return self._size == 0
    
    # Get the top item of the stack
    def peek(self):
        if self.is_empty():
            raise Exception("Peeking from an empty stack")
        return self.head.next.value
    
    # Push a value into the stack.  
    def push(self, value):
        node = Node(value)
        node.next = self.head.next
        self.head.next = node
        self._size += 1

    # Remove a value from the stack and return.  [ 1, 2, 3, 4]
    def pop(self):
        if self.is_empty():
            raise Exception("popping from an empty stack")
        remove = self.head.next
        self.head.next = self.head.next.next
        self._size -= 1
        return remove.value
    
# Driver Code
if __name__ == "__main__":
    stack = Stack()
    for i in range(1, 11):
        stack.push(i)
    print(f"Stack: {stack}")
 
    for _ in range(1, 6):
        remove = stack.pop()
        print(f"Pop: {remove}")
    print(f"Stack: {stack}")


"""
Advantages of Stack:
Stacks are simple data structures with a well-defined set of operations, which makes them easy to understand and use.
Stacks are efficient for adding and removing elements, as these operations have a time complexity of O(1).
In order to reverse the order of elements we use the stack data structure.
Stacks can be used to implement undo/redo functions in applications.

Drawbacks of Stack:
Restriction of size in Stack is a drawback and if they are full, you cannot add any more elements to the stack.
Stacks do not provide fast access to elements other than the top element.
Stacks do not support efficient searching, as you have to pop elements one by one until you find the element you are looking for.
"""