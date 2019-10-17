#!/usr/bin/python3

import sys, threading

sys.setrecursionlimit(10**8) # max depth of recursion
threading.stack_size(2**26)  # new thread will get stack of such size


def IsBinarySearchTree(tree):
    if not tree:
        return True

    def isBST(idx, val_l, val_r):
        val, l, r = tree[idx]
        if (val_l is not None and val < val_l) or (val_r is not None and val >= val_r):
            return False
        else:
            return (l < 0 or isBST(l, val_l, val)) and (r < 0 or isBST(r, val, val_r))

    return isBST(0, None, None)


def main():
    nodes = int(sys.stdin.readline().strip())
    tree = []
    for i in range(nodes):
        tree.append(list(map(int, sys.stdin.readline().strip().split())))
    if IsBinarySearchTree(tree):
        print("CORRECT")
    else:
        print("INCORRECT")

threading.Thread(target=main).start()
