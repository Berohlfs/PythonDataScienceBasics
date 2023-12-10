character = 'a'  # Global variable


def changeCaracter():
    character = 'b'  # Local variable


# In the example below, the printed character will actually be 'a',
# despite of the 'changeCharater()' function call.
# This is because Python treats the two 'character' variables as two different variables.

print('\nWithout the "global" statement...')
changeCaracter()
print(character)

# In order to make the local and global variables the same, you should use the 'global' statement
# inside the function. Check the example below:


def changeCaracter2():
    # Avoid using global variables as much as possible (decrease in modularity and flexibility)
    global character
    character = 'b'


print('\nUsing the "global" statement...')
changeCaracter2()
print(character)
