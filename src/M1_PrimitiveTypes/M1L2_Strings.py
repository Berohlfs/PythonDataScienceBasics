# String concatenation
first_name = ' BerNArDo '
last_name = 'RoHlFS'

print('Concatenation:' + first_name + ' ' + last_name)

# String interpolation (f-strings or formatted strings)
print(f'\nInterpolation: {first_name} {last_name}')

# The 'len' function returns the amount of elements inside an iterable object (future notes)
# Strings are considered iterable objects:
print('\nAmount of characters:' + len(first_name))

# String methods
print('\nString methods:')
print('Upper -> ' + first_name.upper())
print('Lower -> ' + first_name.lower())
print('Title -> ' + first_name.title())
print('Strip -> ' + first_name.strip())
print('RStrip -> ' + first_name.rstrip())
print('LStrip -> ' + first_name.lstrip())
print('Find -> ' + first_name.find('o'))
print('Replace -> ' + first_name.replace('o', '(REPLACED)'))
print('In? -> ' + 'Hello' in first_name)
print('Not in? -> ' + 'Hello' not in first_name)

# Indexes are used to return a portion of elements inside an iterable object (future notes)
# As said previously, strings are considered iterable objects:
print('\nString indexes:')
print(
    first_name[0],
    first_name[-1],
    first_name[1:4],
    first_name[3:],
    first_name[:3],
    # 'start : stop : step' notation. (a negative step inverts the access direction)
    first_name[0::2],
    first_name[::-1]
)

# Obs: Strings are immutable.
# This means that the only way to update a string is to define a new value
# to it's variable.
