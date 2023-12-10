# Comparison operators (numbers)
print('\nComparison operators (numbers):')
print(10 > 10)
print(10 >= 10)
print(10 < 5)
print(10 == 15)
print(10 == '10')  # False. Remember, Python does not provide type coersion.
print(10 != '10')

# Comparison operators (strings)
print('\nComparison operators (strings):')
print("bag" > "apple")  # True. Analyses alphabetical order
print("bag" == "BAG")  # False. 'B' and 'b' are different in ASCII table.

# Ord function
print('\nOrd function:')
print(ord('B'))  # Converts a single character into its integer representation


# Falsy values

# Empty lists
# Empty tuples
# Empty dictionaries
# Empty sets
# Empty strings
# Empty ranges
# Zero (0, 0.0 or even 0j)
# None
# False

# Truthy values

# Non empty lists, tuples, dictionaries, sets, strings or ranges
# Numbers different from zero
# True
