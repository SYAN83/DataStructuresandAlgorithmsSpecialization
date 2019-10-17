# Uses python3
import sys


def gcd_naive(a, b):
    return gcd_naive(b, a % b) if b else a


def lcm_naive(a, b):
    return a * b // gcd_naive(a, b)


if __name__ == '__main__':
    input_ = sys.stdin.read()
    a, b = map(int, input_.split())
    print(lcm_naive(a, b))

