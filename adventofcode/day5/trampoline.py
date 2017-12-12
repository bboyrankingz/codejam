def jumps(lst, fun, marker=0):
    count = -1
    while True:
        count += 1
        try:
            jump = lst[marker]
            if fun(jump):
                lst[marker] = jump - 1
            else:
                lst[marker] = jump + 1
            marker += jump
        except:
            return count


if "__main__" in __name__:

    with open("puzzle") as jump_file:
        reader = jump_file.read()
        sequence = [int(line) for line in reader.split("\n")]

    sequence2 = sequence.copy()
    print(jumps(sequence, lambda x: False))
    print(jumps(sequence2, lambda x: x >= 3))
