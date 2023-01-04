
def my_range(start: int, stop: int, step: int = 1):
    """
    Generator for getting all numbers in the given range.

    :param start: Generator start sequence from this number.
    :param stop: Generator stop generating sequence when current number become bigger than "stop".
    :param step: Add this number to each previous number in sequence.
    :return: Processed number.
    """
    number = start

    while True:
        if number >= stop:
            break
        yield number
        number += step
