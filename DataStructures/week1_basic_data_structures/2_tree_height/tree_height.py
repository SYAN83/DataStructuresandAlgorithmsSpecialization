# python3

import sys
import threading


def compute_height(n, parents):
    heights = [0] * n

    def find(node):
        if heights[node] == 0:
            if parents[node] == -1:
                heights[node] = 1
            else:
                find(parents[node])
                heights[node] = heights[parents[node]] + 1

    for i in range(n):
        find(i)
    return max(heights)


def main():
    n = int(input())
    parents = list(map(int, input().split()))
    print(compute_height(n, parents))


# In Python, the default limit on recursion depth is rather low,
# so raise it here for this problem. Note that to take advantage
# of bigger stack, we have to launch the computation in a new thread.
sys.setrecursionlimit(10**7)  # max depth of recursion
threading.stack_size(2**27)   # new thread will get stack of such size
threading.Thread(target=main).start()
