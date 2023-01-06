import functools


@functools.cache
def factorial(n):
    for i in range(1, n):
        n *= i
    return n if n else 1
    # return n * factorial(n - 1) if n else 1 # raises recursion error if n is too large