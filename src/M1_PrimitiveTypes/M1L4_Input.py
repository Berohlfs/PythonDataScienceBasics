# The 'input' function collects data from the user in the terminal.
# Data collected by the input function is of type string.
# Some scenarios demand type casting, since Python doesn't provide type coersion.
# Not enforcing the adequate type would result in a Type Error.
# Possible type casting functions are: int(), float(), bool() and str().
res = input('Type a number: ')
print('Informed data multiplied by 10: ' + int(res) * 10)

# The 'type' function returns the type of the value passed as parameter.
print(f'\nType of the input: {type(res)}')
