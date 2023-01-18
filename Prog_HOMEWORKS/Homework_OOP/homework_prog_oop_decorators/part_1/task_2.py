from typing import Callable


def references_to_funcs(func: Callable):
    """
    Keeps in references to functions, that was called with this decorator.

    :param func: Function.
    :return Function with arguments.
    """
    funcs = []

    def inner(*args, **kwargs):
        funcs.append(func)
        print(funcs)

        return func(*args, **kwargs)

    return inner


@references_to_funcs
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
