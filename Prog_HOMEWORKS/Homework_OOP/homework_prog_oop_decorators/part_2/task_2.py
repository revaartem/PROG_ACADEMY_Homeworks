
class StrAdderDecorator:
    """
    Add additional text (set as parameter of decorator) to __str__ func of class.
    """

    def __init__(self, text):
        self.text = text

    def __call__(self, func):
        def inner(*args, **kwargs):
            data = self.text + func(*args, **kwargs)
            return data
        return inner


class A:

    def __init__(self, a, b):
        self.a = a
        self.b = b

    @StrAdderDecorator('Hello: ')
    def __str__(self):
        return f'{self.a}x{self.b}'


class B:

    def __init__(self, a, b):
        self.a = a
        self.b = b

    @StrAdderDecorator('World: ')
    def __str__(self):
        return f'{self.a}x{self.b}'


if __name__ == "__main__":
    x = A(5, 3)
    q = B(5, 8)

    print(x)
    print(q)
