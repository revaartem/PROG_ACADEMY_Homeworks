import timeit


def memoiz_fibonacci():
    """
    Getting number of Fibonacci sequence with memoization method.

    :return: Number from Fibonacci sequence.
    """
    result = {}

    def fibonacci(n: int):
        """
        Classic Fibonacci number function with modification for memoization
        of results.

        :param n: Sequence number.
        :return: Number from sequence.
        """
        if not isinstance(n, int):
            raise TypeError

        if n < len(result):
            return result[n]

        if n in (1, 2):
            result[n] = 1
            return 1

        res = fibonacci(n - 1) + fibonacci(n - 2)
        result[n] = res
        return res

    return fibonacci


def fibonacci_classic(num: int):
    """
    Classic Fibonacci number function.

    :param num: Sequence number.
    :return: Number from sequence.
    """
    if not isinstance(num, int):
        raise TypeError

    if num in (1, 2):
        return 1
    return fibonacci_classic(num - 1) + fibonacci_classic(num - 2)


test_memo = """
def memoiz_fibonacci():
    result = {}

    def fibonacci(n):
        if n < len(result):
            return result[n]
        if n in (1, 2):
            result[n] = 1
            return 1
        res = fibonacci(n - 1) + fibonacci(n - 2)
        result[n] = res
        return res
    return fibonacci

func = memoiz_fibonacci()
func(40)
func(13)
func(12)
func(11)
func(10)
func(9)
func(8)
func(7)

"""

test_fibo = """
def fibonacci(n):
    if n in (1, 2):
        return 1
    return fibonacci(n - 1) + fibonacci(n - 2)
    
fibonacci(40)
fibonacci(13)
fibonacci(12)
fibonacci(11)
fibonacci(10)
fibonacci(9)
fibonacci(8)

"""

if __name__ == "__main__":
    mem_time = timeit.timeit(test_memo, number=1)
    fib_time = timeit.timeit(test_fibo, number=1)
    print(mem_time)
    print(fib_time)