"""
Exercise 05
"""

# Input function and type conversion / casting
print('\nInput function:')
# Data collected by the input function is of type string.
# Some scenarios demands type casting, since Python doesn't provide type coersion.
# Not applying the conversion would result in a Type Error.
# Possible type casting functions are: int(), float(), bool() and str().
res = input('Type a number: ')
print(int(res) + 1)

# Type function
print('\nType function:')
print(type(res))

# Falsy values

# Empty lists
# Empty tuples
# Empty dictionaries
# Empty sets
# Empty strings
# Empty ranges
# Zero (0, 0.0 or even 0j)
# None
# False

# Truthy values

# Non empty lists, tuples, dictionaries, sets, strings or ranges
# Numbers different from zero
# True
