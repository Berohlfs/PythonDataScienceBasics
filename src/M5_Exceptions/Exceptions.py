# During the execution of a program, errors might occur due to multiple reasons:

# --> bad data input
# --> developer's mistakes
# --> unavailable resources
# Others...

# These errors oftenly cause the program the crash. Therefore, the goal of treating
# exceptions is to avoid crashes and ensure that a program runs gracefully and offers
# good feedback during execution.

# EXAMPLE
# The function below represents a crash scenario.
# We can foresee that the program will crash if the user types a string,
# considering that the string's value can't be converted into an integer.

def echoNumber():
    while True:
        res = int(input('>'))
        if res == 0:
            print('BREAK')
            break
        print(res)

# That's why we should put it inside a 'try except' block,
# which works similar to the JS 'try catch' block.

try:
    echoNumber()
except ValueError: # Should inform the expected exception.
    print('You did not type a number. Try again')
    echoNumber()
