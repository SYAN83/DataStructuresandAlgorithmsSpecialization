#Uses python3

import sys


def lcs3(a, b, c):
    dp = [[[0] * (len(c) + 1) for _ in range(len(b) + 1)] for _ in range(len(a) + 1)]
    for i, x in enumerate(a):
        for j, y in enumerate(b):
            for k, z in enumerate(c):
                if x == y == z:
                    dp[i + 1][j + 1][k + 1] = dp[i][j][k] + 1
                else:
                    dp[i + 1][j + 1][k + 1] = max(dp[i + 1][j + 1][k], dp[i][j + 1][k + 1], dp[i + 1][j][k + 1])
    return dp[-1][-1][-1]


if __name__ == '__main__':
    input = sys.stdin.read()
    data = list(map(int, input.split()))
    an = data[0]
    data = data[1:]
    a = data[:an]
    data = data[an:]
    bn = data[0]
    data = data[1:]
    b = data[:bn]
    data = data[bn:]
    cn = data[0]
    data = data[1:]
    c = data[:cn]
    print(lcs3(a, b, c))
