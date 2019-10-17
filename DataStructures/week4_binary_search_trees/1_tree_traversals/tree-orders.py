# python3

import sys, threading
sys.setrecursionlimit(10**6) # max depth of recursion
threading.stack_size(2**27)  # new thread will get stack of such size


class TreeOrders:
    def read(self):
        self.n = int(sys.stdin.readline())
        self.key = [0] * self.n
        self.left = [0] * self.n
        self.right = [0] * self.n
        for i in range(self.n):
            self.key[i], self.left[i], self.right[i] = map(int, sys.stdin.readline().split())

    def inOrder(self):
        self.result = list()

        def traverse(idx):
            if idx > -1:
                traverse(self.left[idx])
                self.result.append(self.key[idx])
                traverse(self.right[idx])

        traverse(0)
        return self.result

    def preOrder(self):
        self.result = []

        def traverse(idx):
            if idx > -1:
                self.result.append(self.key[idx])
                traverse(self.left[idx])
                traverse(self.right[idx])

        traverse(0)
        return self.result

    def postOrder(self):
        self.result = []

        def traverse(idx):
            if idx > -1:
                traverse(self.left[idx])
                traverse(self.right[idx])
                self.result.append(self.key[idx])

        traverse(0)
        return self.result


def main():
    tree = TreeOrders()
    tree.read()
    print(" ".join(str(x) for x in tree.inOrder()))
    print(" ".join(str(x) for x in tree.preOrder()))
    print(" ".join(str(x) for x in tree.postOrder()))


threading.Thread(target=main).start()
