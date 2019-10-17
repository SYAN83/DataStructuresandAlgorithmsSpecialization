# Uses python3


def calc_fib(n):
    if n < 2:
        return n
    else:
        a, b, i = 0, 1, 1
        while i < n:
            a, b = b, a + b
            i += 1
        return b


n = int(input())
print(calc_fib(n))
