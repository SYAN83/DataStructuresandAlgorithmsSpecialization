#python3
import sys


class StackWithMax(object):

    def __init__(self):
        self._stack = list()
        self._track = list()

    def push(self, a):
        self._stack.append(a)
        if self._track:
            self._track.append(max(self._track[-1], a))
        else:
            self._track.append(a)

    def pop(self):
        assert(len(self._stack))
        self._track.pop()
        return self._stack.pop()

    def max(self):
        assert(len(self._stack))
        return self._track[-1]


if __name__ == '__main__':
    stack = StackWithMax()
    num_queries = int(sys.stdin.readline())
    for _ in range(num_queries):
        query = sys.stdin.readline().split()
        if query[0] == "push":
            stack.push(int(query[1]))
        elif query[0] == "pop":
            stack.pop()
        elif query[0] == "max":
            print(stack.max())
        else:
            assert 0
