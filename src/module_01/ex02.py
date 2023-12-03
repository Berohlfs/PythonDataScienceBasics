"""
Exercise 02
"""

# Concatenation
print('\nConcatenation:')
first_name = ' BerNArDo'
last_name = 'RoHlFS '
full_name = first_name + ' ' + last_name
print(full_name)

# Interpolation (f-strings or formatted strings)
print('\nInterpolation:')
print(f'{first_name} {last_name}')

# String methods
print('\nString methods:')
print(full_name.upper())
print(full_name.lower())
print(full_name.title())
print(full_name.strip())
print(full_name.rstrip())
print(full_name.lstrip())
print(full_name.find('o'))
print(full_name.replace('o', '(REPLACED)'))
print('Hello' in full_name)
print('Hello' not in full_name)
