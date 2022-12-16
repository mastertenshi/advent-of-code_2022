
class Folder:
    def __init__(self, name, parent):
        self.name = name
        self.parent = parent
        self.children = []
        self.size = 0

    def __str__(self):
        return f"(dir) {self.name} {self.size}"

    def __repr__(self):
        return self.__str__()
  
    def __lt__(self, other):
        return self.size < other.size

    def print_tree(self, tabs=0):
        print("\t" * tabs + f"- {self.name} (dir, size={self.size})")
        tabs += 1
        for f in self.children:
            if isinstance(f, Folder):
                f.print_tree(tabs)
            elif isinstance(f, File):
                print("\t" * tabs + f"- {f.name} (file, size={f.size})")
                
    def add_size(self, size):
        self.size += size
        if self.parent is not None:
            self.parent.add_size(size)


class File:
    def __init__(self, name, size, parent):
        self.name = name
        self.size = size
        self.parent = parent

    def __str__(self):
        return self.name

    def __repr__(self):
        return self.__str__()


class Range:
    def __init__(self, start, end) -> None:
        self.start = int(start)
        self.end = int(end)

    def is_subrange(self, other):
        return (self.start >= other.start) and (self.end <= other.end)

    def is_overlapping(self, other):
        return not (
            (self.start > other.end and self.end > other.start) or
            (self.start < other.end and self.end < other.start))


class Node:
    def __init__(self, x=0, y=0, parent=None, child=None):
        self.x = x
        self.y = y
        self.parent = parent
        self.child = child

    def move(self, x, y):
        self.x += x
        self.y += y

    def __str__(self):
        return f"({self.x}, {self.y})"

    def __repr__(self):
        return self.__str__()


class Monkey:
    def __init__(self, items, op, test, if_true, if_false):
        self.items = items
        self.op = op
        self.test = test
        self.if_true = if_true
        self.if_false = if_false
        self.inspection_count = 0

    def __str__(self):
        return f"Count: {self.inspection_count} | {self.items}"

    def __repr__(self):
        return self.__str__()
