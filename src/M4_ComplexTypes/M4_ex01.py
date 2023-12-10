# Lists contain a sequence of elements. These elements can belong to any type.
letters = ['a', 'b', 'c']
numbers = [1, 2, 3, 4]
matrix = [[1, 2], [3, 4]]

# Python is really smart and powerful. Check this out:
zeros = [0] * 5
print(f'\nMultiplying a list: {zeros}')

letters_and_numbers = letters + numbers
print(f'\nJoining two different lists: {letters_and_numbers}')

# There is an even faster way to create certain lists. Using the 'list' function.
# This function receives an iterable object as a parameter.
print(f'\nThe "list" function: \n -> {list(range(1, 6))} \n -> {list("Bernardo")}')

# The 'len' function can be used on any iterable object, including lists:
print(f'\nLength of a list: {len(zeros)}')
