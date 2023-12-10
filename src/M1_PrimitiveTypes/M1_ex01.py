# Variables
# Python's primitive types are: integer, float, boolean and string.
number_int = 5
number_float = 5.5
string = 'Hello world!'
boolean = True

# Long strings
long_string = """Hi John,
How are you doing?"""

# Print function
print('\nPrinting a number' + number_int)

# Len function
print('\nAmount of characters:' + len(long_string))

# String indexes
print('\nString indexes:')
print(
    string[0],
    string[-1],
    string[1:4],
    string[3:],
    string[:3]
)

# Escape character
# An escape character is a backslash (\) followed by the character you want to insert.
# Escape sequences examples: \', \", \n
# print('\') --> Error. '\' is a special character. Fix this using a escape sequence:
print('\nEscape characters: \\, \', \"')
