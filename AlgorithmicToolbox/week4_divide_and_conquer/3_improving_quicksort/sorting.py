# Uses python3
import sys
import random


def partition3(a, l, r):
    x = a[l]
    i, j, k = l+1, l, r
    while i < k:
        if a[i] < x:
            a[i], a[j] = a[j], a[i]
            i += 1
            j += 1
        elif a[i] > x:
            k -= 1
            a[i], a[k] = a[k], a[i]
        else:
            i += 1
    return j, k


def partition2(a, l, r):
    x = a[l]
    j = l
    for i in range(l + 1, r + 1):
        if a[i] <= x:
            j += 1
            a[i], a[j] = a[j], a[i]
    a[l], a[j] = a[j], a[l]
    return j


def randomized_quick_sort(a, l, r):
    if r - l < 2:
        return
    k = random.randrange(l, r)
    a[l], a[k] = a[k], a[l]
    # use partition3
    m, n = partition3(a, l, r)
    randomized_quick_sort(a, l, m)
    randomized_quick_sort(a, n, r)


if __name__ == '__main__':
    input = sys.stdin.read()
    n, *a = list(map(int, input.split()))
    randomized_quick_sort(a, 0, n)
    for x in a:
        print(x, end=' ')
