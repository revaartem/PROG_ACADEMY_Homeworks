
class MetaHandler(type):
    """
    This class intercepts information about the class being processed and
    write it to 'meta_data.txt'.
    """

    def __new__(typeclass, classname, supers, classdict):
        return type.__new__(typeclass, classname, supers, classdict)

    def __init__(self, classname, supers, classdict: dict):
        with open('meta_data.txt', 'a') as file:
            file.write(f'{classname}, {[item for item in classdict]}\n')


class Box(metaclass=MetaHandler):

    def __init__(self, a, b, c):
        self.a = a
        self.b = b
        self.c = c


if __name__ == "__main__":
    box_1 = Box(5, 9, 8)