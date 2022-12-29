
def g_progression(start_number: int, multiplier: int):
    """
    Simple generator of geometrical progression.\n
    To stop generator type "<generator object>.close()"

    :param start_number: Generator start progression from this number.
    :param multiplier: Generator multiply each previous number on this number
    :return: Processed number.
    """
    number = start_number

    while True:
        yield number * multiplier
        number *= multiplier
