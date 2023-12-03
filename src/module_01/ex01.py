"""
Exercise 01
"""

# Python's primitive types are: number, boolean and string.

# Variables
number = 5
string = 'Hello world!'
boolean = True

# Long strings
long_string = """Hi John,
How are you doing?"""

# Print function
print('\nPrint function:')
print(number)
print(string)
print(boolean)
print(long_string)

# Len function
print('\nLen function:')
print(len(long_string))

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
print('\nEscape characters:')
print('\\')
