"""
Exercise 07
"""

# 'if' statement
temperature = 28
if temperature > 30:
    print('It\'s hot!')
elif temperature > 0:
    print('It\'s okay...')
else:
    print('it\'s freezing!')

print('done')

# Ternary operator
random_number = 2 if temperature > 30 else 1
print(random_number)

# Logical operators (and, or, not)
# These operators follow a short-circuit evaluation
if random_number == 2 and temperature < 30:
    print('Yep...')
else:
    print('Nope...')

# Chaining operators
if 0 < temperature < 30:
    print('ok')
