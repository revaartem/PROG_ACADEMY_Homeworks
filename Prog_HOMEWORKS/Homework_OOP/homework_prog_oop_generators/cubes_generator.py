
def cubes_generator(stop: int):
    """
    Generator for getting all numbers from 2 to "stop" in the third degree.

    :param stop: Generator stop generating sequence when current number become bigger than "stop".
    :return: Number ** 3
    """
    number = 2

    while True:
        if number >= stop:
            break
        yield number ** 3
        number += 1

print(list(cubes_generator(150)))
