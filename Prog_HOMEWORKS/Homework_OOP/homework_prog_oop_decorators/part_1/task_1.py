from typing import Callable


def call_counter(func: Callable):
    """
    Counting the quantity of function calls.

    :param func: Function.
    :return: Function with arguments.
    """
    counter = {}

    def inner(*args, **kwargs):
        nonlocal counter
        if not counter.get(func.__name__):
            counter[func.__name__] = 1
        else:
            counter[func.__name__] += 1

        return func(*args, **kwargs)

    return inner


@call_counter
def cubes(num: int):
    """
    Raises number to the 3rd power.

    :param num: Number to process.
    :return: Number ** 3.
    """
    if not isinstance(num, int):
        raise TypeError
    num **= 3
    return num


if __name__ == "__main__":
    cubes(5)
    cubes(5)
    cubes(5)
