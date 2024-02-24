"""
O(1): Constant complexity. The runtime is constant, regardless of the size of the input.

O(log n): Logarithmic complexity. The runtime increases logarithmically with the size of the input.

O(n): Linear complexity. The runtime increases linearly with the size of the input.

O(n log n): Linearithmic complexity. Common in efficient sorting algorithms like merge sort and heap sort.

O(n^2): Quadratic complexity. The runtime is proportional to the square of the size of the input.

O(2^n): Exponential complexity. The runtime increases exponentially with the size of the input.

O(n!): Factorial complexity. The runtime increases factorially with the size of the input.


Common Python Function Complexities:
List:
acess an element by index list[1]: O(1)
insersion or removal at the end of the list: list.append(1), list.pop() O(1)
insersion or removal at the beginning or in the middle of the list O(n)

Dictionaries:
Insertion, retrieval, or removal of an element: O(1) on average (can be O(n) in rare collision cases)

Sets:
Insertion, retrieval, or removal of an element: O(1) on average

Strings:
Concatenation: O(n)
Accessing a character by index: O(1)

Sorting:
Efficient algorithms like merge sort and heap sort: O(n log n)
Bubble sort algorithm: O(n^2)

sort() and sorted() of python is O(n log n) as well and they use the TimSort algorithm
"""

# in summary dict, set, tuples, and strings are O(1) for insertion, retrieval, and removal
# lists are O(1) for insertion and removal at the end, but O(n) for insertion and removal at the beginning or in the middle
# sorting is O(n log n) for efficient algorithms and O(n^2) for bubble sort
# concatenation is O(n) for strings
