from typing import Callable


def str_file_writer(func: Callable):
    """
    Write result of __str__ function to {name_of_function}.txt file.

    :param func: Function.
    :return: Function with arguments.
    """
    def inner(reference, *args, **kwargs):
        name = type(reference).__name__

        with open(f"{name}.txt", 'w') as file:
            file.write(func(reference))

        return func(reference)

    return inner