import datetime
from typing import Callable


def time_decorator(func: Callable):
    """
    Calculate the running time of the function in a certain range of cycles, results saves to
    'running_time_result.txt'.

    Parameters 'cycles' and 'folder' sets inside the function.

    :param func: Function.
    :return: None
    """

    cycles = 100
    folder = 'running_time_result.txt'

    def inner(*args, **kwargs):

        date_start = datetime.datetime.now()
        for _ in range(cycles):
            func(*args, **kwargs)
        date_finish = datetime.datetime.now()

        actual_running_time = date_finish - date_start

        with open(folder, 'a') as file:

            if actual_running_time.seconds:
                file.write(f'{func.__name__} {actual_running_time.seconds}.{actual_running_time.microseconds} sec\n')
            else:
                file.write(f'{func.__name__} 0.{actual_running_time.microseconds} sec\n')

    return inner


@time_decorator
def cubes(num: int):
    """
    Raises number to the 3rd power.

    :param num: Number to process.
    :return: Number ** 3.
    """
    if not isinstance(num, int):
        raise TypeError
    num **= 50000
    return num


if __name__ == "__main__":
    cubes(5)