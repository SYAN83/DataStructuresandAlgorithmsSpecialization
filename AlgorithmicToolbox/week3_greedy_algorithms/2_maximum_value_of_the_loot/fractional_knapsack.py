# Uses python3
import sys


def get_optimal_value(capacity, weights, values):
    value, weight = 0., capacity
    loot = sorted(zip(weights, values), key=lambda x: x[0] / x[1])
    for w, v in loot:
        if weight > w:
            value += v
            weight -= w
        else:
            value += weight * v / w
            break
    return value


if __name__ == "__main__":
    data = list(map(int, sys.stdin.read().split()))
    n, capacity = data[0:2]
    values = data[2:(2 * n + 2):2]
    weights = data[3:(2 * n + 2):2]
    opt_value = get_optimal_value(capacity, weights, values)
    print("{:.10f}".format(opt_value))
