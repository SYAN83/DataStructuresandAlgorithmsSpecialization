# Uses python3
import sys


def fibonacci_last_digit_cumsum(k):
    cumsum = [0, 1]
    previous, current = 1, 2
    while not (previous == cumsum[0] and current == cumsum[1]):
        cumsum.append(cumsum[-1] + previous)
        previous, current = current, (previous + current) % k
    return cumsum


def fibonacci_sum_naive(n):
    cumsum = fibonacci_last_digit_cumsum(10)
    res = (n // len(cumsum)) * cumsum[-1] + cumsum[n % len(cumsum)]
    return res % 10


if __name__ == '__main__':
    input = sys.stdin.read()
    n = int(input)
    print(fibonacci_sum_naive(n))
