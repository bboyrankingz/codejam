
def sumall(puzzles, fun):
    return sum([fun(puzzle) for puzzle in puzzles])


def checksum(puzzle):
    return max(puzzle) - min(puzzle)


def checksum2(puzzle):
    puzzle = sorted(puzzle, reverse=True)
    i = -1
    while i < len(puzzle):
        i += 1
        for j in range(i + 1, len(puzzle)):
            divid = puzzle[i] / puzzle[j]
            if divid.is_integer():
                return int(divid)


if "__main__" in __name__:
    input_file = open("input")
    read = input_file.readlines()
    print(sumall([[int(numbers) for numbers in line[:-1].split("\t")] for line in read], checksum))
    print(sumall([[int(numbers) for numbers in line[:-1].split("\t")] for line in read], checksum2))
