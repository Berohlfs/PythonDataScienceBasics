# Variables can belong to different scopes: 'local' or 'global'.

character = 'a'  # Global variable. Available to the whole module/script.


def changeCaracter():
    character = 'b'  # Local variable. Available only to the function context.

# The 'global' statement...

# In the example below, the printed character will actually be 'a',
# despite of the 'changeCharater()' function call.
# This is because Python treats the two 'character' variables as different.

print('\nWithout the "global" statement...')
changeCaracter()
print(character)

# In order to make the local and global variables the same, you should use the 'global' statement
# inside the function. Check the example below:


def changeCaracter2():
    # Avoid using global variables as much as possible, as they decrease modularity and flexibility.
    global character
    character = 'b'


print('\nUsing the "global" statement...')
changeCaracter2()
print(character)
