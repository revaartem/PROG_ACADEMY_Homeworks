from abc import ABC, abstractmethod
import sympy


class SimpleNums(ABC):
    @abstractmethod
    def number_is_simple(self):
        if sympy.isprime(self.num):
            return True
        else:
            return False


class Sample(SimpleNums):

    def __init__(self, num):
        self.num = num

    def number_is_simple(self):
        if sympy.isprime(self.num):
            return True
        else:
            return False


class OtherSample:

    def __init__(self, num):
        self.num = num

    def number_is_simple(self):
        if sympy.isprime(self.num):
            return True
        else:
            return False


if __name__ == "__main__":
    first = Sample(2)
    print(first.number_is_simple())

    second = OtherSample(2)
    print(second.number_is_simple())

    SimpleNums.register(OtherSample)
    print(issubclass(OtherSample, SimpleNums))
