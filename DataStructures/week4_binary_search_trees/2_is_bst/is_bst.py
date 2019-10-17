#!/usr/bin/python3

import sys, threading

sys.setrecursionlimit(10**8) # max depth of recursion
threading.stack_size(2**26)  # new thread will get stack of such size


def IsBinarySearchTree(tree):
    if not tree:
        return True

    def isBinary(root):
        v, l, r = tree[root]
        vll, vlr, vrl, vrr = v, None, None, v
        if l > -1:
            l_, vll, vlr = isBinary(l)
            if l_ is False:
                return False, 0, 0
        if r > -1:
            r_, vrl, vrr = isBinary(r)
            if r_ is False:
                return False, 0, 0
        if (vlr is None or vlr < v) and (vrl is None or v <= vrl):
            return True, vll, vrr
        else:
            return False, 0, 0

    return isBinary(0)[0]


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
