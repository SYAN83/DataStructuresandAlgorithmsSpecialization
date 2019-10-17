# python3


def build_heap(data):
    """Build a heap from ``data`` inplace.

    Returns a sequence of swaps performed by the algorithm.
    """
    n = len(data)
    swaps = list()

    def swap(i):
        left, right = 2 * i + 1, 2 * i + 2
        min_ = i
        if left < n and data[i] > data[left]:
            min_ = left
        if right < n and data[min_] > data[right]:
            min_ = right
        if min_ != i:
            data[i], data[min_] = data[min_], data[i]
            swaps.append([i, min_])
            swap(min_)

    for i in range(n // 2)[::-1]:
        swap(i)
    return swaps


def main():
    n = int(input())
    data = list(map(int, input().split()))
    assert len(data) == n

    swaps = build_heap(data)

    print(len(swaps))
    for i, j in swaps:
        print(i, j)


if __name__ == "__main__":
    main()
