# Uses python3
import sys

def binary_search(a, x):
    left, right = 0, len(a)

    def search(l, r):
        if l < r:
            mid = (l + r) // 2
            if a[mid] == x:
                return mid
            else:
                return search(l, mid) if a[mid] > x else search(mid+1, r)
        else:
            return -1

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
    a = data[1 : n + 1]
    for x in data[n + 2:]:
        # replace with the call to binary_search when implemented
        print(binary_search(a, x), end=' ')
