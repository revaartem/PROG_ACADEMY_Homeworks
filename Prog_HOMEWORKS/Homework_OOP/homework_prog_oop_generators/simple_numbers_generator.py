import sympy


def simple_numbers_generator(start: int, stop: int):
    """
    Generator for getting simple numbers in the given range.

    :param start: Generator start sequence from this number.
    :param stop: Generator stop generating sequence when current number become bigger than "stop".
    :return: Simple number in range(start, stop)
    """
    number = start

    while True:
        if number >= stop:
            break
        if sympy.isprime(number):
            yield number
        number += 1
