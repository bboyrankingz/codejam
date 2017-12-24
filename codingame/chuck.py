from itertools import repeat


def gen(it):
    a = [it[0]]
    for i in it[1:]:
        if i in a:
            a.append(i)
        else:
            yield a
            a = [i]
    yield a


def encode_like_chuck(message):
    binary_m = "".join((format(ord(l), 'b').zfill(7) for l in message))
    tab = " ".join(["".join(("0 " if i[0] == "1" else "00 ", "".join(repeat("0", len(i))))) for i in gen(binary_m)])
    return tab


if "__main__" in __name__:
    assert encode_like_chuck("%") == "00 0 0 0 00 00 0 0 00 0 0 0"
