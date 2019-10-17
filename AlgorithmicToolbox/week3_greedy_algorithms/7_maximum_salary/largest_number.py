#Uses python3
import sys


class StringInteger(str):

    def __lt__(self, other):
        return self + other < other + self

    def __gt__(self, other):
        return self + other > other + self


def largest_number(a):
    a_ = sorted([StringInteger(x) for x in a], reverse=True)
    return ''.join(a_)


if __name__ == '__main__':
    input = sys.stdin.read()
    data = input.split()
    a = data[1:]
    print(largest_number(a))

