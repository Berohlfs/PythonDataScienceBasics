# Map function =================================|

# The map function receives an iterable
# object and returns a modified version of it

numbers = [1, 2, 3, 4]

# Note the anonymous function
mapped_numbers = map(lambda number: number*2, numbers)

# The map function returns a 'map object'. You can easily turn it
# into a list using the 'list' function.

print(f'\n Mapped: {list(mapped_numbers)}')

# Filter function ================================|

# The list function is very similar to the map function.
# The main diference is that, instead of returning the result of an operation, the
# lambda function should return the result of a condition (a boolean value).

words = ['abc', 'bcdef', 'cdefghij', 'de']

# Returns a 'filter' object
filtered_words = filter(lambda word: len(word) >= 5, words)

print(f'\n Filtered: {list(filtered_words)}')

# List Comprehensions ================================|

# List comprehensions are able to filter and map iterable objects
# just as well as the 'map' and 'filter' functions.
# However, they are simpler and do not come from a 'functional background'.
# note that they don't rely on lambda functions:

mapped_numbers = [number * 2 for number in numbers]
print(f'\n Mapped with comprehensions: {mapped_numbers}')

filtered_words = [word for word in words if len(word) >= 5]
print(f'\n Filtered with comprehensions: {filtered_words}')

# You can use mapping and filtering comprehensions together.
# Besides, using comprehensions allows you to not use the 'list' function

# Zip function ================================|

# The zip function accepts multiple iterable objects as arguments.
# It is capable of combining the elements of each object, at
# every given position, into tuples inside a 'zip object'.
# Note that these tuples will be formed for as long as there are
# available elements on each object at a given position.

mytuple = (1, 2, 3)

mylist = ['a', 'b', 'c']

myzip = zip(mytuple, mylist, [True, False, True])

print(f'\n Zipped: {list(myzip)}')
