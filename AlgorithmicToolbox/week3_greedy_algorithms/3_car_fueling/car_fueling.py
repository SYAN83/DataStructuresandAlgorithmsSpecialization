# python3
import sys


def compute_min_refills(distance, tank, stops):
    stops_ = stops + [distance]
    refill, cap = 0, tank
    for i in range(len(stops)):
        if cap < stops_[i]:
            return -1
        elif cap < stops_[i + 1]:
            refill += 1
            cap = stops_[i] + tank
    return -1 if cap < distance else refill


if __name__ == '__main__':
    d, m, _, *stops = map(int, sys.stdin.read().split())
    print(compute_min_refills(d, m, stops))
