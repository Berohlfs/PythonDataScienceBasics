# While loop (flag oriented)
print('\n While loop')
number = 100
while number > 80:
    number -= 1
    print(number)

# Infinite loop (condition is always true)
# To get out of an infinite loop, a 'break' statement is necessary
print('\n While loop (infinite)')

while True:
    command = input('>')
    print(command)
    if command.lower() == 'quit':
        break
