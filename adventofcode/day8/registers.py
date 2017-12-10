class Register(object):

    def __init__(self, cache={}):
        self.cache = cache

    def parse_modify(self, sequence):
        chaine, modify, number = sequence.split(" ")
        if modify == "inc":
            return chaine, int(number)
        return chaine, -1 * int(number)

    def parse_condition(self, sequence):
        chaine, modify, number = sequence.split(" ")
        if not self.cache.get(chaine):
            self.cache[chaine] = 0
        if modify == ">":
            return self.cache[chaine] > int(number)
        elif modify == ">=":
            return self.cache[chaine] >= int(number)
        elif modify == "<":
            return self.cache[chaine] < int(number)
        elif modify == "<=":
            return self.cache[chaine] <= int(number)
        return self.cache[chaine] == int(number)

    def register(self, sequence):
        return self.cache