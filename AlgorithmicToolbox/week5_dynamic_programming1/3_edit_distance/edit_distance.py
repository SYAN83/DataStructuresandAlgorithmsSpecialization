# Uses python3


def edit_distance(s, t):
    m, n = len(s)+1, len(t)+1
    dp = [[0] * n for _ in range(m)]
    for i in range(1, m):
        dp[i][0] = i
    for j in range(1, n):
        dp[0][j] = j
    for i, p in enumerate(s):
        for j, q in enumerate(t):
            dp[i+1][j+1] = min(dp[i][j] - (p == q), dp[i+1][j], dp[i][j+1]) + 1
    return dp[-1][-1]


if __name__ == "__main__":
    print(edit_distance(input(), input()))
