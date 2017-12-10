class Register(object):

    def __init__(self, cache={}):
        self.cache = cache
        self.greatest = 0

    def parse_modify(self, sequence):
        chaine, modify, number = sequence.split(" ")
        if not self.cache.get(chaine):
            self.cache[chaine] = 0
        if modify == "inc":
            return chaine, int(number)
        return chaine, -1 * int(number)

    def parse_condition(self, sequence):
        chaine, *to_eval = sequence.split(" ")
        if not self.cache.get(chaine):
            self.cache[chaine] = 0
        return eval("{}{}".format(self.cache[chaine], " ".join(to_eval)))

    def register(self, sequence):
        modify, condition = sequence.split(" if ")
        key, value = self.parse_modify(modify)
        if self.parse_condition(condition):
            self.cache[key] = self.cache[key] + value
            if self.cache[key] > self.greatest:
                self.greatest = self.cache[key]
        return self.cache


if "__main__" in __name__:
    registry = Register()
    with open("puzzles") as input_file:
        for sequence in input_file.readlines():
            registry.register(sequence)
    print(max([v for k, v in registry.cache.items()]))
    print(registry.greatest)
