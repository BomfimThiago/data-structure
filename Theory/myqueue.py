"""
    Firs-In/First-Out(FIFO)
    consumers are good example of queues

    Operations associated with queue are: 

    Enqueue: Adds an item to the queue. If the queue is full, then it is said to be an Overflow condition – 
    Time Complexity : O(1)
    
    Dequeue: Removes an item from the queue. The items are popped in the same order in which they are pushed. 
    If the queue is empty, then it is said to be an Underflow condition – Time Complexity : O(1)
    
    Front: Get the front item from queue – Time Complexity : O(1)
    
    Rear: Get the last item from queue – Time Complexity : O(1)

    In python we can implement stacks following 3 ways
    - list
    - Collections.deque
    - queue.Queue
"""

# implementing with a list
queue = []
queue.append('a')
queue.append('b')
queue.append('c')
print("Initial queue")
print(queue)
print("\nElements dequeued from queue")
print(queue.pop(0))
print(queue.pop(0))
print(queue.pop(0))
print("\nQueue after removing elements")
print(queue)


# implementing with collections.deque
"""
Queue in Python can be implemented using deque class from the collections module.

Deque is preferred over list in the cases where we need quicker append and pop operations from both the ends of container,
as deque provides an O(1) time complexity for append and pop operations as compared to list which provides O(n) time complexity. 
Instead of enqueue and deque, append() and popleft() functions are used.

The code uses a deque from the collections module to represent a queue. It appends ‘a’, ‘b’, and ‘c’ to 
the queue and dequeues them with q.popleft(), resulting in an empty queue. Uncommenting q.popleft() after the queue 
is empty would raise an IndexError. The code demonstrates queue operations and handles an empty queue scenario.
"""
from collections import deque
q = deque()
q.append('a')
q.append('b')
q.append('c')
print("Initial queue")
print(q)
print("\nElements dequeued from the queue")
print(q.popleft())
print(q.popleft())
print(q.popleft())
 
print("\nQueue after removing elements")
print(q)


# implementing using queue.Queue
"""
Queue is built-in module of Python which is used to implement a queue. queue.Queue(maxsize) initializes a variable to a maximum size of maxsize. A maxsize of zero ‘0’ means a infinite queue. This Queue follows FIFO rule. 
There are various functions available in this module: 

maxsize – Number of items allowed in the queue.
empty() – Return True if the queue is empty, False otherwise.
full() – Return True if there are maxsize items in the queue. If the queue was initialized with maxsize=0 (the default), then full() never returns True.
get() – Remove and return an item from the queue. If queue is empty, wait until an item is available.
get_nowait() – Return an item if one is immediately available, else raise QueueEmpty.
put(item) – Put an item into the queue. If the queue is full, wait until a free slot is available before adding the item.
put_nowait(item) – Put an item into the queue without blocking. If no free slot is immediately available, raise QueueFull.
qsize() – Return the number of items in the queue.
"""