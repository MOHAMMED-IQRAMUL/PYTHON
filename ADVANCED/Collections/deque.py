from collections import deque
"""
This script demonstrates the usage of the `deque` class from the `collections` module in Python.
A `deque` (double-ended queue) is a generalization of stacks and queues that supports adding and removing elements from either end with approximately O(1) performance. It is especially useful for implementing queues, stacks, or other data structures where fast appends and pops from both ends are required.
Examples:
    # Importing deque
    # Creating a deque
    # Adding elements to the deque
    queue.append('A')  # Add to the right
    queue.appendleft('B')  # Add to the left
    # Accessing elements
    print(queue)  # Output: deque(['B', 'A'])
    # Removing elements
    queue.pop()  # Remove from the right
    queue.popleft()  # Remove from the left
    # Checking if deque is empty
    print(len(queue) == 0)  # Output: True
    # Rotating elements
    queue.extend([1, 2, 3, 4])
    queue.rotate(2)  # Rotate to the right by 2
    print(queue)  # Output: deque([3, 4, 1, 2])
    # Clearing the deque
    queue.clear()
    print(queue)  # Output: deque([])
Attributes:
    - `append(x)`: Add `x` to the right end of the deque.
    - `appendleft(x)`: Add `x` to the left end of the deque.
    - `pop()`: Remove and return an element from the right end of the deque.
    - `popleft()`: Remove and return an element from the left end of the deque.
    - `extend(iterable)`: Extend the right side of the deque by appending elements from the iterable.
    - `extendleft(iterable)`: Extend the left side of the deque by appending elements from the iterable (in reverse order).
    - `rotate(n)`: Rotate the deque `n` steps to the right. If `n` is negative, rotate to the left.
    - `clear()`: Remove all elements from the deque.
"""

queue = deque()
