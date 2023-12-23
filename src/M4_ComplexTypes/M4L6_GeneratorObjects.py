from sys import getsizeof

# Generator objects

# Generator objects are special because they do not store in memory
# all of their elements. Instead, their elements are generated 'on iteration time'.
# This means that they are amazingly small and perfect for very large data objects.

# To prove this, let's import the 'getsizeof' method from the 'sys' module

generator = (number * 2 for number in range(1000)) # Use tuples to create generators

print(f'\nGenerator: {generator}')

print(f"\nGenerator's size: {getsizeof(generator)}\n")

for index, number in enumerate(generator):
    print('>' + str(number))
    if index > 5:
        print('...')
        break


print(f'\n List size: {getsizeof([number * 2 for number in range(1000)])}')

# Note that generator objects have no 'len'. That's
# because it's not possible to know their length.

# ========================= IMPORTANT =========================

# UNPACKING OPERATOR

# Unpacking operators are similar to the 'spread'
# operator from JS, with some sutil differences.

# In JavaScript, destructuring assignment and spread operators work together.
# In Python, this may happen to the '*' (non-key-value) unpacking operator.
# However, the '**' (key-value) unpacking operator is used for spreading only, not destructuring.

# EXAMPLE (this does not work):

# obj = {item: item * 2 for item in range(5)}
# first, *others = obj

# UNPACKING IS REALLY POWERFUL. It allows you to make complex
# operations with lists, sets, dictionaries, etc.
