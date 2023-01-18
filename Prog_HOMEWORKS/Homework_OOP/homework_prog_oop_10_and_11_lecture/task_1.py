
class Descriptor:
    """
    Descriptor with read-only value.
    """

    def __init__(self, value):
        self.value = value

    def __get__(self, inst_self, inst_class):
        return self.value

    def __set__(self, inst_self, value):
        raise ValueError ('Read only parameter')

    def __delete__(self, inst_self):
        raise ValueError ('Read only parameter')


class Box:

    def __init__(self, a, b, c):
        self.a = a
        self.b = b
        self.c = c

    color = Descriptor('Orange')


if __name__ == "__main__":
    box_1 = Box(2, 3, 5)
    print(box_1.color)
    box_1.color = 'green'