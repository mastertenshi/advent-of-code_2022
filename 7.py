from models_7 import Folder, File
import utils


def find_folder(name, parent_folder):
    folders = list(filter(lambda f: isinstance(f, Folder) and f.name == name, parent_folder.children))
    if len(folders) == 1:
        return folders[0]
    return None


text = utils.get_input("7.txt")

root = Folder("/", None)
curr_folder = root

is_ls = False
for line in text.split("\n")[1:]:
    line = line.strip()
    
    if line.startswith("$ ls"):
        is_ls = True
        continue
    
    if line.startswith("$ cd"):
        is_ls = False
        location = line[line.rindex(" ")+1:]
        if location == '..':
            curr_folder = curr_folder.parent
        elif location == '/':
            curr_folder = root
        else:
            curr_folder = find_folder(location, curr_folder)

    if is_ls:
        if line.startswith("dir"):
            folder = Folder(line.split(" ")[1], curr_folder)
            curr_folder.children.append(folder)
        else:
            file = File(*line.split(" ")[::-1], parent=curr_folder)
            curr_folder.children.append(file)
            curr_folder.add_size(int(file.size))


def part_one(folder):
    sum = 0
    for f in folder.children:
        if isinstance(f, Folder):
            sum += part_one(f)
            if f.size <= 100_000:
                sum += f.size
    return sum


def part_two(folder):
    dirs = []
    for f in folder.children:
        if isinstance(f, Folder):
            dirs += part_two(f)
            if f.size >= 30_000_000 - (70_000_000 - root.size):
                dirs.append(f)
    return dirs


print(f"Sum: {part_one(root)}")
print(f"Folder to delete: {sorted(part_two(root))[0]}")
