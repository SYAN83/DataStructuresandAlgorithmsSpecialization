# Uses python3
import sys


def get_change(m):
    if m < 1:
        return 0
    coins = [c for c in (1, 3, 4) if c <= m]
    changes = [-1] * m
    for coin in coins:
        changes[coin-1] = 1
    for i in range(m):
        if changes[i] == -1:
            changes[i] = min(changes[i-c] for c in coins if i >= c) + 1
    return changes[-1]


if __name__ == '__main__':
    m = int(sys.stdin.read())
    print(get_change(m))
