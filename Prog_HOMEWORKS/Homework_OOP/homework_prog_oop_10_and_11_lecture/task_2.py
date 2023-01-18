
class Box:

    def __init__(self, a, b, c):
        self.a = a
        self.b = b
        self.c = c

    def __setattr__(self, key, value):
        if not isinstance(value, int):
            raise TypeError
        self.__dict__[key] = value


if __name__ == "__main__":
    box_1 = Box(2, 3, 4)

    box_1.weight = 6
    print(box_1.weight)
    box_1.color = 'green'
    