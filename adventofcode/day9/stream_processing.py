
def stream(sequence, step=1):
    if len(sequence) == 0:
        return 0
    for i in range(len(sequence)):
        if sequence[i] == "{":
            print(sequence[i+1:len(sequence) - i - 1])
            step = step + stream(sequence[i+1:len(sequence) - i - 1], step + 1)
            break
    return step
