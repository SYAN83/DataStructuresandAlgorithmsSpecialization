# Uses python3
import sys


def fibonacci_last_digit_cumsum(k):
    cumsum = [0, 1]
    previous, current = 1, 2
    while not (previous == cumsum[0] and current == cumsum[1]):
        cumsum.append(cumsum[-1] + previous)
        previous, current = current, (previous + current) % k
    return cumsum


def fibonacci_partial_sum_naive(from_, to):
    cumsum = fibonacci_last_digit_cumsum(10)
    a, b = cumsum[(from_ - 1) % len(cumsum)] if from_ > 0 else 0, cumsum[to % len(cumsum)]
    res = (to - from_) // len(cumsum) * cumsum[-1] - a + b
    return res % 10


if __name__ == '__main__':
    input = sys.stdin.read();
    from_, to = map(int, input.split())
    print(fibonacci_partial_sum_naive(from_, to))