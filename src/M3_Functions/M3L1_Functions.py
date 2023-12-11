# A function is a block of code which only runs when it is called.
# You can pass data, known as parameters, into a function.

def count():
    """Function with no return value (void): () -> None"""
    for number in range(1, 5):
        print(f'Number {number}...')


def getGreeting(name: str):
    """Function with a return value: (name: str) -> str"""
    return f'Hi, {name}! Nice to meet you!'


def increment(number: int, by: int = 1):
    """Function with optional parameters"""
    return number + by


def testXargs(*numbers: int):
    """Function with 'xargs'.
    This special parameter is used to gather all argument data
    into a single variable inside a function.
    They are defined as tuples (future notes)"""
    print(numbers)


def testXxargs(**person):
    """Function with 'xxargs'.
    Another special parameter used for the same purpouse.
    However, they are defined as dictionaries (future notes)"""
    print(person)


# Now, let's call all the functions above:
count()
print(getGreeting(name='Bernardo'))
print(increment(1))
testXargs(1, 2, 3, 4, 5)
testXxargs(name='Bernardo', age=21)
