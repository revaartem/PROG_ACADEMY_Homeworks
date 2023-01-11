from typing import Callable


def sum_func(func: Callable[[int], int]):
    """
    The function takes another function as an argument and
    returns the sum of the elements of the list processed
    by the given function.

    :param func: Function to process the list.
    :return: Sum of processed list.
    """
    if not isinstance(func, Callable):
        raise TypeError
    numbers = list(range(1, 11))

    processed_numbers = []

    for number in numbers:
        processed_numbers.append(func(number))

    return sum(processed_numbers)


def cubes(num: int):
    """
    Raises number to the 3rd power.

    :param num: Number to process.
    :return: Number ** 3.
    """
    num **= 3
    return num


if __name__ == "__main__":
    test = sum_func(cubes)
    print(test)
