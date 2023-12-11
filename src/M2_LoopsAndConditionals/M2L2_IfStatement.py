# If statements specify a block of code to be executed if a condition is true.
print('\nHow is the weather?')

temperature = 28
if temperature > 25:
    print('It\'s hot!')
elif temperature > 0:
    print('It\'s cool...')
else:
    print('it\'s freezing!')

# Ternary operators are a shorter version of 'if' statements.
print(f'\nConditional number: {2 if temperature > 30 else 1}')

# Logical operators (and, or, not) are used to build more complex and refined conditions.
# These operators follow a short-circuit evaluation
print('\nLogical operators:')
fruit = 'banana'
if temperature < 25 and fruit == 'banana':
    print('Yep...')
else:
    print('Nope...')

# Chaining operators are a way to use logical operators implicitly
print('\nChaining operators:')
if 0 < temperature < 30:
    print('Temperature is between 0 and 30.')
