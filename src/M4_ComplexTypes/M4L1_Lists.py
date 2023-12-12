# Lists are iterable objects that contain a sequence
# of elements. These elements can belong to any type.
letters = ['a', 'b', 'c']
numbers = [1, 2, 3, 4]
matrix = [[1, 2], [3, 4]]

# Python is really smart and powerful. Check this out:
zeros = [0] * 5
print(f'\nMultiplying a list: {zeros}')

letters_and_numbers = letters + numbers
print(f'\nJoining two different lists: {letters_and_numbers}')

# There is an even faster way to create certain lists: using the 'list' function.
# This function receives an iterable object as a parameter.
print(
    f'\nThe "list" function: \n -> {list(range(1, 6))} \n -> {list("Bernardo")}')

# The 'len' function can be used on any iterable object, including lists:
print(f'\nLength of a list: {len(zeros)}')

# In the same way as strings, all iterable objects can be indexed. Check this out:
# Note that when using the ':' command, the returned value is
# a sub list, not a single element.
print('\nList indexes:')
print(
    numbers[0],
    numbers[-1],
    numbers[1:4],
    numbers[3:],
    numbers[:3],
    numbers[0::2],
    numbers[::-2]
)

# Differently from strings, lists are MUTABLE.
# This means you can change a single element of a list
# by simply accessing one of it's indexes and updating the value inside.

numbers[0] = 1000
print(f'\nUpdated list: {numbers}')

# Unpacking a list to multiple variables.
# Obs: in Python, the amount of variables MUST be equal to the amount of values in the array.
number1, number2, number3, number4 = numbers
print(f'\nNumber 01 -> {number1}')
# however, if a list has too many elements, there are a few alternatives:
number1, number2 = numbers[0:2]
print(f'\nNumber 02 -> {number2}')
# Or use the spread syntax to attribute the surplus list to a new variable
number1, *others = numbers
print(f'\nOthers (end) -> {others}')
number1, *others, last = numbers
print(f'\nOthers (middle) -> {others}')

# Fun fact --> You CAN unpack strings!!

# Looping over lists
print('\nLooping over lists')
for number in numbers:
    print(number)

# The enumerate function
# # numbers will now be a tuple (index, value)
print('\nUsing the enumerate function')
for number in enumerate(numbers):
    print(number[0])
    # You can also unpack 'number'. Ex: `for index, value in numbers:`
