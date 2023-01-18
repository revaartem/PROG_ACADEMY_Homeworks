
class Box:

    def __init__(self, a, b, c):
        self.a = a
        self.b = b
        self.c = c

    def volume(self):
        return self.a * self.b * self.c

    @staticmethod
    def summary_volume(box_1, box_2):
        return box_1.volume() + box_2.volume()


if __name__ == "__main__":
    box_one = Box(2, 3, 5)
    box_two = Box(2, 8, 7)

    data = Box.summary_volume(box_one, box_two)
    print(data)
