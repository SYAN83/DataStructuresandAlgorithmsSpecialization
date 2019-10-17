# python3
import sys


def compute_min_refills(distance, tank, stops):
    # write your code here
    stops.append(distance)
    refil, cap = 0, tank
    for i in range(len(stops)-1):
        if cap < stops[i]:
            return -1
        elif cap < stops[i+1]:
            refil += 1
            cap = stops[i] + tank
    return -1 if cap < distance else refil


if __name__ == '__main__':
    d, m, _, *stops = map(int, sys.stdin.read().split())
    print(compute_min_refills(d, m, stops))
