class Tubes(object):

    def __init__(self, puzzles):
        self.puzzles = puzzles
        self.path = ""
        self.step = 0

    def start(self, line=0):
        column = self.puzzles[line].index("|")
        return self.moove(line + 1, column, (1, 0))

    def moove(self, line, column, direction):
        self.step += 1

        if self.puzzles[line][column] == " ":
            return

        x, y = direction

        while self.puzzles[line][column] in ["|", "-"]:
            self.step += 1
            line += x
            column += y

        if self.puzzles[line][column] == "+":
            if y == 0:
                if column - 1 >= 0 and self.puzzles[line][column - 1] != " ":
                    return self.moove(line, column - 1, (0, -1))
                return self.moove(line, column + 1, (0, 1))
            if line - 1 >= 0 and len(self.puzzles[line - 1]) > column and self.puzzles[line - 1][column] != " ":
                return self.moove(line - 1, column, (-1, 0))
            return self.moove(line + 1, column, (1, 0))

        self.path += self.puzzles[line][column]
        return self.moove(line + x, column + y, direction)


def parse_puzzle_line(line):
    return list(line)


if "__main__" in __name__:
    with open("puzzles") as input_file:
        puzzles = [list(line[:-1]) for line in input_file.readlines()]
        tubes = Tubes(puzzles)
        tubes.start()
        print(tubes.path)
        print(tubes.step)


