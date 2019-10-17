# Uses python3
import sys


def partition3(A):
    sum_ = sum(A)
    if sum_ % 3:
        return 0
    else:
        n = sum_ // 3
        dp = [[0] * (n+1) for _ in range(n+1)]
        dp[0][0] = 1
        for a in A:
            for i in range(n, -1, -1):
                for j in range(n, -1, -1):
                    if dp[i][j]:
                        if i + a <= n:
                            dp[i + a][j] = 1
                        if j + a <= n:
                            dp[i][j + a] = 1
            if dp[-1][-1]:
                return 1
        return 0


if __name__ == '__main__':
    input = sys.stdin.read()
    n, *A = list(map(int, input.split()))
    print(partition3(A))

