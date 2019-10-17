# Uses python3
import sys


def optimal_weight(W, w):
    n = len(w)
    dp = [[0] * (W + 1) for _ in range(n + 1)]
    for i in range(n):
        for wt in range(1, W + 1):
            dp[i + 1][wt] = dp[i][wt]
            if w[i] <= wt:
                v = dp[i][wt - w[i]] + w[i]
                if v > dp[i + 1][wt]:
                    dp[i + 1][wt] = v
    return dp[n][W]


if __name__ == '__main__':
    input = sys.stdin.read()
    W, n, *w = list(map(int, input.split()))
    print(optimal_weight(W, w))
