# Uses python3
import sys

def get_change(m):
    count = 0
    for c in [10, 5]:
        count += m // c
        m %= c
    return count + m


if __name__ == '__main__':
    m = int(sys.stdin.read())
    print(get_change(m))
