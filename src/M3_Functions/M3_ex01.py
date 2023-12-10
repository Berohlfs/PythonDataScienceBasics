def count(limit: int):
    """counts from one to the number provided"""
    for number in range(1, limit + 1):
        print(f'Number {number}...')


def getGreeting(name: str | int):
    """Returns a formatted greeting for the name provided"""
    return f'Hi, {name}! Nice to meet you!'  # Default return value is 'None'


def increment(number: int, by: int = 1):
    """Optional parameters must be declared after the required ones"""
    return number + by


def testXargs(*numbers: int):  # xargs are defined as tuples (future exercises)
    print(numbers)


def testXxargs(**person):  # xxargs are defined as dictionaries (future exercises)
    print(person)


# Now, let's call the functions above:
# Obs: Adding the keyword argument to an argument, although unnecessary,
# can improve readability in certain scenarios
count(3)
print(getGreeting(name='Bernardo'))
print(increment(1))
testXargs(1, 2, 3, 4, 5)
testXxargs(name='Bernardo', age=21)
