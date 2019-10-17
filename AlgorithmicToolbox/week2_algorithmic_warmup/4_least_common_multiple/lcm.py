# Uses python3
import sys


def lcm_naive(a, b):

    def gcd_naive(a, b):
        return gcd_naive(b, a % b) if b else a

    return a // gcd_naive(a, b) * b


if __name__ == '__main__':
    input = sys.stdin.read()
    a, b = map(int, input.split())
    print(lcm_naive(a, b))

