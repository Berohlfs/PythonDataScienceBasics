# For loop
print('\nExample 01: range method with 1 parameter.')
for i in range(3):  # 3 iterations (indexes: 0, 1 and 2)
    print(f'Attempt {i + 1}', '.' * (i + 1))

print('\nExample 02: range method with 2 parameters.')
for i in range(1, 4):  # 2 iterations (indexes: 1, 2 and 3)
    print(f'Attempt {i}', '.' * (i))

print('\nExample 03: range method with 3 parameters.')
for i in range(0, 10, 2):
    print(f'Attempt {i}', '.' * (i))

# For else
print('\nFor Else:')

success = True
for i in range(3):
    print(f'Attempt {i + 1}')
    if success:
        print('Got it!')
        break
else:
    print('This is printed if the loop is completed.')

# Nested
print('\nNested loops:\n')

for x in range(5):
    for y in range(5):
        print(f'({x}, {y})')

# We have already seen Python's primitive types (number, string, boolean).
# However, Python also offers complex types (future notes).
# There are a bunch of complex types that are iterable:
# type 'range', for example is iterable (can be looped over)
print(f'\nType of range: {type(range(5))}\n')
# Strings are also iterable:
for character in 'Bernardo':
    print(character.upper())
