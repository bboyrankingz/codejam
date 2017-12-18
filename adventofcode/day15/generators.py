remainder = 2147483647


def gen(start, factor, r=5):
    for i in range(r):
        start = start * factor % remainder
        yield start


def to_binary(iterable):
    for i in iterable:
        binary = '{0:08b}'.format(i)
        while len(binary) < 32:
            binary = "0" + binary
        yield binary


def compare(iterable1, iterable2, r=5):
    for i in range(r):
        bin1 = iterable1.__next__()
        bin2 = iterable2.__next__()
        for j in range(16):
            if bin1[0 + j: 0 + j + 16] == bin2[0 + j: 0 + j + 16]:
                yield 1
                break


if "__main__" in __name__:
        # print(len([_ for _ in compare(to_binary(gen(591, 16807, 40000000)),
        #                               to_binary(gen(393, 48271, 40000000)), 40000000)]))

        print(len([_ for _ in compare(to_binary(gen(65, 16807, 40000000)),
                                      to_binary(gen(8921, 48271, 40000000)), 40000000)]))
