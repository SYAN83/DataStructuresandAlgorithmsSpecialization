# Uses python3
import sys


def binary_search(a, x):

    def search(left, right):
        if left < right:
            mid = (left + right) // 2
            if a[mid] > x:
                return search(left, mid)
            elif a[mid] < x:
                return search(mid + 1, right)
            else:
                return mid
        else:
            return -1

    left, right = 0, len(a)
    return search(left, right)


def linear_search(a, x):
    for i in range(len(a)):
        if a[i] == x:
            return i
    return -1


if __name__ == '__main__':
    input = sys.stdin.read()
    data = list(map(int, input.split()))
    n = data[0]
    m = data[n + 1]
    a = data[1: n + 1]
    for x in data[n + 2:]:
        # replace with the call to binary_search when implemented
        print(binary_search(a, x), end=' ')
