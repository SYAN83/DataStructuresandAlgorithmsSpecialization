# Uses python3
import sys


def get_optimal_value(capacity, weights, values):
    order_items = sorted([v / w, v, w] for w, v in zip(weights, values))
    weight = 0
    value = 0
    while order_items and weight < capacity:
        p, v, w = order_items.pop()
        if weight + w > capacity:
            value += p * (capacity - weight)
            break
        else:
            weight += w
            value += v
    return value


if __name__ == "__main__":
    data = list(map(int, sys.stdin.read().split()))
    n, capacity = data[0:2]
    values = data[2:(2 * n + 2):2]
    weights = data[3:(2 * n + 2):2]
    opt_value = get_optimal_value(capacity, weights, values)
    print("{:.10f}".format(opt_value))
