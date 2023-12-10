# If statement
print('\nHow is the weather?')

temperature = 28
if temperature > 30:
    print('It\'s hot!')
elif temperature > 0:
    print('It\'s okay...')
else:
    print('it\'s freezing!')

# Ternary operator
conditional_number = 2 if temperature > 30 else 1
print(f'Random number: {conditional_number}')

# Logical operators (and, or, not)
# These operators follow a short-circuit evaluation
print('\nLogical operators:')
if conditional_number == 2 and temperature < 30:
    print('Yep...')
else:
    print('Nope...')

# Chaining operators
print('\nChaining operators:')
if 0 < temperature < 30:
    print('ok')
