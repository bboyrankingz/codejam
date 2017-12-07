import sys


def captcha(puzzle):
    more = puzzle[0] if puzzle[0] == puzzle[len(puzzle) - 1] else 0
    return sum([puzzle[i] for i in range(len(puzzle) - 1) if puzzle[i] == puzzle[i + 1]]) + more


def captcha2(puzzle):
    def condition(i):
        cursor = round(len(puzzle) / 2) + i
        if cursor >= len(puzzle):
            cursor = cursor - len(puzzle)
        return puzzle[i] == puzzle[cursor]

    return sum([puzzle[i] for i in range(len(puzzle)) if condition(i)])


if "__main__" in __name__:
    print(captcha([int(_) for _ in sys.argv[1]]))
    print(captcha2([int(_) for _ in sys.argv[1]]))
