# Uses python3
import sys
import math


def optimal_summands(n):
    k = int((math.sqrt(n * 8 + 1) - 1) // 2)
    summands = [i + 1 for i in range(k)]
    for i in range(n - k * (k + 1) // 2):
        summands[-1-i] += 1
    return summands


if __name__ == '__main__':
    input = sys.stdin.read()
    n = int(input)
    summands = optimal_summands(n)
    print(len(summands))
    for x in summands:
        print(x, end=' ')
