
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
