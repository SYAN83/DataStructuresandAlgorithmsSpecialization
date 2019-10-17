# Uses python3
import sys

coins = (1, 3, 4)


def get_change(m):
    if m < 1:
        return 0
    changes = [-1] * m
    for i in range(m):
        if i + 1 in coins:
            changes[i] = 1
        else:
            changes[i] = min(changes[i-c] for c in coins if i >= c) + 1
    return changes[-1]


if __name__ == '__main__':
    m = int(sys.stdin.read())
    print(get_change(m))
