# Uses python3


def calc_fib(n):
    if n < 2:
        return n
    else:
        a, b = 0, 1
        while n > 1:
            a, b = b, a + b
            n -= 1
        return b


if __name__ == '__main__':
    n = int(input())
    print(calc_fib(n))
