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

# Set comprehensions
set_comprehension = {number * 2 for number in first}
print(f'\nSet comprehension: {set_comprehension}')

# Dictionaries =============================|

# Dictionaries are data structures that contain 'key-value' pairs.
# Keys must belong to immutable types (strings, tuples, integers, etc).

person = {
    'name': 'Bernardo',
    'age': 21,
    0: 'Example of numeric key'
}

print(f'\nPerson: {person}')
# A dictionary attribute can't be indexed. Instead, use the property's name.
print(f'Age: {person["age"]}')

# You can also create a dictionary with the 'dic' constructor
second_person = dict(name='João', age=19)

# Add new properties...
second_person['new_prop'] = 'blabla'

# Delete property...
del second_person['age']

print(f'\n2º Person: {second_person}')
print(f'Name: {second_person["name"]}')

# Check existence of a key...
if 'new_prop' in second_person:
    print('Existe!!')

# Or
# 0 is the default value in case 'age' isn't found
print(second_person.get('age', 0))

# Obs: When we iterate over a dictionary, the values returned on
# each iteration will be the dictionarie's keys
# However...
# --> 'dic.values()' will return the values.
# --> 'dic.items()' will return the pairs as tuples in an array (VERY USEFUL FOR SORTING AND MORE).

# Dictionary comprehensions
dictionary_comprehension = {number: number * 2 for number in range(5)}
print(f'\nDictionary comprehension: {dictionary_comprehension}')
