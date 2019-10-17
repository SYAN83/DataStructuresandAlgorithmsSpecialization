# python3


def are_matching(left, right):
    matches = {'(': ')', '[': ']', '{': '}'}
    return matches[left] == right


def find_mismatch(text):
    opening_brackets_stack = []
    for i, x in enumerate(text):
        if x in '([{':
            opening_brackets_stack.extend([i, x])
        elif x in ')]}':
            if opening_brackets_stack and are_matching(opening_brackets_stack.pop(), x):
                opening_brackets_stack.pop()
            else:
                return i + 1
    else:
        return opening_brackets_stack[-2] + 1 if opening_brackets_stack else 'Success'


def main():
    text = input()
    mismatch = find_mismatch(text)
    print(mismatch)


if __name__ == "__main__":
    main()
