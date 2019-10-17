# python3
import heapq


def max_pairwise_product(numbers):
    num_ = numbers[:2]
    for n in numbers[2:]:
        heapq.heappushpop(num_, n)
    return num_[0] * num_[1]


if __name__ == '__main__':
    input_n = int(input())
    input_numbers = [int(x) for x in input().split()]
    print(max_pairwise_product(input_numbers))
