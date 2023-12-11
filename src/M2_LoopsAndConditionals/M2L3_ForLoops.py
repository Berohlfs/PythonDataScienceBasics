# For loops are used for iterating over an iterable object, in, other words, a sequence.

# The 'range' function is the easiest way to generate a iterable sequence in Python.
print('\nExample 01: range method with 1 parameter.')
for i in range(3):  # 3 iterations (indexes: 0, 1 and 2)
    print(f'Attempt {i + 1}.')

print('\nExample 02: range method with 2 parameters.')
for i in range(1, 4):  # 2 iterations (indexes: 1, 2 and 3)
    print(f'Attempt {i + 1}.')

print('\nExample 03: range method with 3 parameters.')
for i in range(0, 10, 2):
    print(f'Attempt {i + 1}.')

# For else
# The 'else' keyword in a for loop specifies a block of code to be executed only
# when the loop is completed.
print('\nFor Else:')

success = True
for i in range(3):
    print(f'Attempt {i + 1}')
    if success:
        print('Got it!')
        break
else:
    print('This is printed if the loop is completed.')

# Nested loops...
print('\nNested loops:\n')

for x in range(5):
    for y in range(5):
        print(f'({x}, {y})')


# Besides primitive types, Python also provides us with complex
# types (future notes), and these are usually iterable.
# However, strings are also iterable:
print('\nIterating a string:\n')
for character in 'Bernardo':
    print(character.upper())
