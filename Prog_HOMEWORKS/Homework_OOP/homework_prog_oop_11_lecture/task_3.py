import datetime


class InformationDuplicate:
    """
    Duplicate all changes of value to 'value_log.txt'.
    """

    def __init__(self, value):
        self.value = value

    def __get__(self, inst_self, inst_class):
        return self.value

    def __set__(self, inst_self, value):
        with open('value_log.txt', 'a') as file:
            file.write(f'New value = {value}, Time: {datetime.datetime.now()}\n')
            self.value = value

    def __delete__(self, inst_self):
        del self.value


class Box:

    def __init__(self, a, b, c):
        self.a = a
        self.b = b
        self.c = c

    color = InformationDuplicate('Orange')


if __name__ == "__main__":
    box_1 = Box(2, 3, 5)
    print(box_1.color)
    box_1.color = 'green'
    box_1.color = 'blue'
    box_1.color = 'black'
    box_1.color = 'yellow'
    box_1.color = 'grey'
