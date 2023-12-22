from array import array

# Tuples ===================|

# Tuples are immutable lists (read only)

first_tuple = (1, 2, 3)
second_tuple = 1, 2, 3  # This is also interpreted by Python as a tuple.
third_tuple = 1,  # This too

# Use the 'tuple' function to transform iterable objects into tuples.

new_tuple = tuple([1, 2, 3])

# In general, tuples are very similar to lists, specially
# from a 'reading' perspective.

# Tuples are really useful for SWAPPING VALUES
# between two variables without using a temp variable. Look:

x = 10
y = 11

x, y = y, x

print(f'\nx: {x}, y: {y}')

# Arrays ===================|

# An array in Python is a data structure very similar to lists.
# However, arrays are used for large amounts of data, since they
# are more performant. This is due to the fact that arrays store
# values that belong to the same type.

# To use arrays, you will need to import the 'array' class from the
# 'array' module.

numbers = array("i", [1, 2, 3])

numbers.append(4)

print(f'\nArray: {numbers}')

# Note that the first parameter indicates the type of the array's elements.
# https://docs.python.org/3/library/array.html --> Check out all typecodes.

# Sets =============================|

# Sets are a data structure that contains a sequence of UNIQUE elements.
# In other words, there can't be two equal elements inside a set object.
# SETS ARE NOT SEQUENCES, THEREFORE IT IS NOT POSSIBLE TO ACCESS
# IT'S VALUES BY INDEXES.

# Sets can be instanced by braces. Look:

my_set = {1, 2, 3}

my_set.add(3)  # won't be added
my_set.remove(1)

print(f'\nMy set: {my_set}')

# Or using the constructor

my_other_set = set([1, 2, 3, 3])

print(f'My other set: {my_other_set}')

# Set operations

first = {1, 2, 3, 4}
second = {3, 4, 5, 6}

print(f'\nConsider {first} and {second}...........................\n')

print(f'Union of both: {first | second}')
print(f'Intersection: {first & second}')
print(f'First - intersection: {first - second}')
print(f'Both - intersection: {first ^ second}')
