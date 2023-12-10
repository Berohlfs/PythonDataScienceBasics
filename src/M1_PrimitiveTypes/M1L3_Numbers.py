import math  # https://docs.python.org/3/library/math.html

# Numbers are an important primitive type.
# We are able to apply them to a bunch of arithmetic operations...

# Operations
print('\nOperations:')
print(5 + 3)
print(5 - 3)
print(5 * 3)
print(5 / 3)
print(5 // 3)  # Floor division
print(5 % 3)
print(5 ** 3)

# Use augmented assignment operators to facilitate variable attribution
num = 3
num += 1  # Instead of 'x = x + 1'
print(f'\nAugmented assignment -> {num}')

# Note: Python offers syntax for complex numbers (a + bi).
# These are commonly used in maths and physics.
complex_number = 1 + 2j

# Python also has some native numberic methods:
print('\nNumber methods:')
number = -5.4
print('Round: ' + round(number))
print('Absolute: ' + abs(number))

# Use the native 'Math' module for more advanced operations:
print('\nMath module methods:')
print('Ceil: ' + math.ceil(number))
print('Floor: ' + math.floor(number))
print('Factorial: ' + math.factorial(abs(round(number))))
