from collections import OrderedDict


class DigitalPlumber(object):

    def __init__(self, tree):
        self.tree = tree
        self.count = 0
        self.group = 0

    def launch(self):
        while len(self.tree) > 0:
            self.group += 1
            self.plumber(self.tree.items()[0][0])

    def plumber(self, start=0):
        sons = self.tree.get(start)
        if sons:
            if self.group <= 1:
                self.count += 1
            del self.tree[start]
            for child in sons:
                self.plumber(child)


if "__main__" in __name__:
    tree = OrderedDict()
    with open("puzzle") as f:
        for line in f.readlines():
            father, sons = line[:-1].split(" <-> ")
            tree[int(father)] = [int(son) for son in sons.split(", ")]

    p = DigitalPlumber(tree)
    p.launch()
    print(p.group)
    print(p.count)
