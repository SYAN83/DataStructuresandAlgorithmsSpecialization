# Uses python3
import sys


def gcd_naive(a, b):
    return gcd_naive(b, a % b) if b else a


if __name__ == "__main__":
    input = sys.stdin.read()
    a, b = map(int, input.split())
    print(gcd_naive(a, b))
