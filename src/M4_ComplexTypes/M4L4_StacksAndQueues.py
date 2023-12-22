from collections import deque

# Stacks and Queues are common data structures.
# Stack --> LIFO (Last In First Out)
# Queue --> FIFO (First In First Out)

# Stacks ===========================|

stack = []

stack.append(1)
stack.append(2)
stack.append(3)

stack.pop()

print(f'\nStack: {stack}')

# Queues ===========================|

# Considering queues remove the first element of a sequence,
# in certain scenarios, using lists can become bad for performance, since
# all elements will need to be relocated back one position.

# With all that considered, in Python, a 'deque' class object is normally used
# to handle queues. This class is imported from Python's built-in module 'collections'.
# This module offers multiple new complex data types.

queue = deque([1, 2, 3])

queue.append(4)

queue.popleft() # Exclusive method

print(f'\nQueue: {queue}')
