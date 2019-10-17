# python3


def read_input():
    return input().rstrip(), input().rstrip()


def print_occurrences(output):
    print(' '.join(map(str, output)))


def get_occurrences(pattern, text):
    result = []
    m, n = len(pattern), len(text)
    p, t, h = 0, 0, 1
    d, q = 256, 101
    for i in range(m - 1):
        h = (h * d) % q
    for i in range(m):
        p = (d * p + ord(pattern[i])) % q
        t = (d * t + ord(text[i])) % q
    for i in range(n - m + 1):
        if p == t and text[i:i+m] == pattern:
            result.append(i)
        if i < n - m:
            t = (d * (t - ord(text[i]) * h) + ord(text[i + m])) % q
            if t < 0:
                t = t + q
    return result


if __name__ == '__main__':
    print_occurrences(get_occurrences(*read_input()))

