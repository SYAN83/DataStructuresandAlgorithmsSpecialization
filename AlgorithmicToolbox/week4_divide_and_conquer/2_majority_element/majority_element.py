# Uses python3
import sys


def get_majority_element(a):
    # Boyer–Moore majority vote algorithm
    maj_index, count = 0, 1
    for i, x in enumerate(a):
        if a[maj_index] == x:
            count += 1
        else:
            count -= 1
        if count == 0:
            maj_index = i
            count = 1
    freq, k = 0, len(a) // 2
    for x in a:
        if x == a[maj_index]:
            freq += 1
        if freq > k:
            return x
    return -1


if __name__ == '__main__':
    input = sys.stdin.read()
    _, *a = list(map(int, input.split()))
    if get_majority_element(a) != -1:
        print(1)
    else:
        print(0)
