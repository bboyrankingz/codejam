def hex(sequence):
    cache = []
    max_step = 0
    step = 0
    for seq in sequence.split(","):
        if seq == "ne":
            cache.append((1, 1))
        elif seq == "sw":
            cache.append((-1, -1))
        elif seq == "nw":
            cache.append((1, -1))
        elif seq == "se":
            cache.append((-1, 1))
        elif seq == "s":
            cache.append((-2, 0))
        elif seq == "n":
            cache.append((2, 0))

        step = int((abs(sum([x for x, y in cache])) + abs(sum([y for x, y in cache]))) / 2)
        if step > max_step:
            max_step = step
    return max_step, step


if "__main__" in __name__:
    with open("puzzle") as input_file:
        seq = input_file.read()
        print(hex(seq))
