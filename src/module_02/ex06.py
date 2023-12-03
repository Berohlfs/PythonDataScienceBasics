"""
Exercise 06
"""

# Comparison operators (numbers)
print('\nComparison operators (numbers):')
print(10 > 10)
print(10 >= 10)
print(10 < 5)
print(10 == 15)
print(10 == '10')  # False. Remember, Python does not provide type coersion.
print(10 != '10')  # False. Remember, Python does not provide type coersion.

# Comparison operators (strings)
print('\nComparison operators (strings):')
print("bag" > "apple")  # Analyses alphabetical order
print("bag" == "BAG")  # False. 'B' and 'b' are different in ASCII table.

# Ord function
print('\nOrd function:')
print(ord('B'))  # Converts a single character into its integer representation
