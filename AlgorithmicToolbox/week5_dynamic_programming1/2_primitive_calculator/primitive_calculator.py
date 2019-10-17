# Uses python3
import sys


def optimal_sequence(n):
    if n == 1:
        return [1]
    ops = min_ops(n)
    return seq_gen(n, ops)


def seq_gen(n, ops):
    seq = []
    while n > 0:
        seq.append(n)
        if n % 2 and n % 3:
            n -= 1
        elif n % 2:
            n = n-1 if ops[n-1] < ops[n//3] else n // 3
        elif n % 3:
            n = n-1 if ops[n-1] < ops[n//2] else n // 2
        else:
            n = n // 2 if ops[n//2] < ops[n//3] else n // 3
    return seq[::-1]


def min_ops(n):
    res = [0] * (n + 1)
    res[0], res[1] = 1, 1
    for i in range(2, n+1):
        x = res[i-1]
        y = i if i % 2 else res[i // 2]
        z = i if i % 3 else res[i // 3]
        res[i] = min(x, y, z) + 1
    return res


if __name__ == '__main__':
    input = sys.stdin.read()
    n = int(input)
    sequence = list(optimal_sequence(n))
    print(len(sequence) - 1)
    for x in sequence:
        print(x, end=' ')
