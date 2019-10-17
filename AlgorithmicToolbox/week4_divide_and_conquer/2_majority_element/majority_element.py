# Uses python3
import sys
from collections import Counter


def get_majority_element(a, left, right):
    count = Counter(a)
    return int(count.most_common(1)[0][1] > len(a) // 2)
    # if left == right:
    #     return -1
    # if left + 1 == right:
    #     return a[left]
    # #write your code here
    # return -1


if __name__ == '__main__':
    input = sys.stdin.read()
    n, *a = list(map(int, input.split()))
    if get_majority_element(a, 0, n):
        print(1)
    else:
        print(0)
