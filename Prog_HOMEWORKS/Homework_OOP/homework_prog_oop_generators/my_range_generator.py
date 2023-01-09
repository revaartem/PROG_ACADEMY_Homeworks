
def my_range(start: int, stop: int, step: int = 1):
    """
    Generator for getting all numbers in the given range.

    :param start: Generator start sequence from this number.
    :param stop: Generator stop generating sequence when current number become bigger than "stop".
    :param step: Add this number to each previous number in sequence.
    :return: Processed number.
    """
    if not isinstance(start, int):
        raise TypeError
    if not isinstance(stop, int):
        raise TypeError
    if not isinstance(step, int):
        raise TypeError

    if not step:
        raise ValueError

    if step < 0 and stop > start:
        return
    if step > 0 and stop < start:
        return

    while abs(start) < abs(stop):
        yield start
        start += step
