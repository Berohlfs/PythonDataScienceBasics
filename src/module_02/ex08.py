"""
Exercise 08
"""

# For loop
# Range
for i in range(3): # 3 iterations (indexes: 0, 1 and 2)
    print(f'Attempt {i + 1}', '.' * (i + 1))

print('\nOR\n')

for i in range(1, 4): # 2 iterations (indexes: 1, 2 and 3)
    print(f'Attempt {i}', '.' * (i))

print('\nAdding a step:\n')

for i in range(0, 10, 2):
    print(f'Attempt {i}', '.' * (i))

# For else
print('\nFor Else:\n')

success = True
for i in range(3):
    print(f'Attempt {i + 1}')
    if(success):
        print('Got it!')
        break
else:
    print('This is printed if the loop is completed.')

# Nested
print('\nNested loops:\n')

for x in range(5):
    for y in range(5):
        print(f'({x}, {y})')
