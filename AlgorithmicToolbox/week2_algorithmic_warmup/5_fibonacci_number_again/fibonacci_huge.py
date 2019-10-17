# Uses python3
import sys


def get_fibonacci_huge_naive(n, m):

    def pisano_period(m):
        previous, current = 0, 1
        for i in range(0, m * m):
            previous, current = current, (previous + current) % m
            if previous == 0 and current == 1:
                return i + 1

    n %= pisano_period(m)

    if n < 2:
        return n % m
    else:
        previous, current = 0, 1
        for i in range(n - 1):
            previous, current = current, (previous + current) % m
        return current


if __name__ == '__main__':
    input = sys.stdin.read()
    n, m = map(int, input.split())
    print(get_fibonacci_huge_naive(n, m))
