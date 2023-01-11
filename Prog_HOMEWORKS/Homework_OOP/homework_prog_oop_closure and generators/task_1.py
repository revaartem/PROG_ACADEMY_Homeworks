from typing import Callable


def mult_by_2(num: int):
    """
    Multiples number by 2.

    :param num: Number to process.
    :return: Number * 2.
    """
    if not isinstance(num, int):
        raise TypeError
    num *= 2
    return num


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


def squares(num: int):
    """
    Raises number to the 2nd power.

    :param num: Number to process.
    :return: Number ** 2.
    """
    if not isinstance(num, int):
        raise TypeError
    num **= 2
    return num


def generator(func: Callable, *args: int):
    """
    Generate numbers according to given function.

    1st argument - Start (default = 1), 2nd - Stop. 3 or more arguments - ValueError(to many arguments)

    :param func: Function that sets the sequence.
    :param args: Arguments for function. 1st argument - Start (default = 1), 2nd - Stop. 3 or more arguments - Error.
    :return: Number of sequence.
    """
    if not isinstance(func, Callable):
        raise TypeError
    if len(args) == 1:
        if not isinstance(*args, int):
            raise TypeError
        start, stop = 1, args

    elif len(args) == 2:
        if not isinstance(args[0], int):
            raise TypeError
        elif not isinstance(args[1], int):
            raise TypeError
        start, stop = args
    elif len(args) > 2:
        raise ValueError ('to many arguments')

    x = func(start)
    stop_num = 1
    for num in range(start + 1, stop):
        yield x
        x = func(num)
        stop_num += 1
        if stop_num > stop:
            break


if __name__ == "__main__":
    res_mult_by_2 = generator(mult_by_2, 2, 20)
    res_cubes = generator(cubes, 2, 20)
    res_squares = generator(squares, 2, 20)
    value_error = generator(squares, 2, 2, 2)

    print(list(res_mult_by_2))
    print(list(res_cubes))
    print(list(res_squares))
    print(list(value_error))
