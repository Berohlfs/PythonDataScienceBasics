numbers = [1, 1, 2, 3, 4, 5]

# SORTING =====================================|

# Returns a sorted copy of a list
print(f'\nSorted copy: {sorted(numbers)}')
# Sorts the original list
print(f'\nSorted original: {numbers.sort(reverse=True)} (Does not return)')

# Both 'sort' and 'sorted' accept a 'REVERSE' parameter of type boolean.

# Both 'sort' and 'sorted' accept a 'KEY' parameter for complex sorting.
# This parameter accepts a callable object, in other words, a function

products = [('Soap', 10), ('Water', 5)]
print(f'\nSorted with key: {sorted(products, key=lambda item:item[0])}')

# Observe the anonymous function syntax used in the example above.

# CHECKING =====================================|

# Checks the existence of an element inside a list
if 2 in numbers:
    print('\n"2" Exists')

# COUNTING =====================================|

# Counts the amount of occurrences of an element inside a list
print(f'\nNumbers of "ones": {numbers.count(1)}')

# ADDING =====================================|

# Adds to the end
numbers.append(6)

# Add 4 to the index '1'
numbers.insert(1, 4)

# FINDING =====================================|

# Finds index of element (1st occurrence)
# ERROR if the element does not exist (should check first)
print(f'\nIndex of "10": {numbers.index(4)}')

# REMOVING =====================================|

# Removes from the end (default)
# ERROR if list is empty (should check first)
numbers.pop()

# Removes the element at the given index.
# ERROR if index is out of range (should check first)
numbers.pop(0)

# Removes the given element (1st occurrence)
# ERROR if element does not exist (should check first)
numbers.remove(4)

# Removes a portion of a list
del numbers[3]

# Removes all
numbers.clear()
