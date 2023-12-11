# While loops are used to execute a block of code for as long as a condition is true.
print('\n While loop')
number = 100
while number > 80:
    number -= 1
    print(number)

# Infinite loops (condition is always true)
# To get out of an infinite loop, a 'break' statement is necessary
print('\n While loop (infinite)')

while True:
    command = input('>')
    print(command)
    if command.lower() == 'quit':
        break

# Obs:
# -> A 'break' statement is used to exit a loop.
# -> A 'continue' statement is used to immediately move on to the next iteration.
# -> A 'pass' statement is used as a placeholder for future code.
