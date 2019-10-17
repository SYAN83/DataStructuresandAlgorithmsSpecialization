# Uses python3
from sys import stdin


def fibonacci_last_digit(k):
    last_digit = [0, 1]
    previous, current = 1, 2
    while not (previous == last_digit[0] and current == last_digit[1]):
        last_digit.append(previous)
        previous, current = current, (previous + current) % k
    return last_digit


def fibonacci_sum_squares_naive(n):
    last_digit = fibonacci_last_digit(10)
    k = n % len(last_digit)
    a, b = last_digit[k - 1], last_digit[k]
    return ((a + b) * b) % 10


if __name__ == '__main__':
    n = int(stdin.read())
    print(fibonacci_sum_squares_naive(n))
