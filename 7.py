from models import Folder, File
import utils

text = utils.get_input("7.txt")

root = Folder("/", None)
curr_folder = root


def cd(input_str):
    global curr_folder

    location = input_str[input_str.rindex(" ") + 1:]
    if location == '..':
        curr_folder = curr_folder.parent
    elif location == '/':
        curr_folder = root
    else:
        curr_folder = find_folder(location, curr_folder)


def add_file(input_str):
    if input_str.startswith("dir"):
        folder = Folder(input_str.split(" ")[1], curr_folder)
        curr_folder.children.append(folder)
    else:
        file = File(*input_str.split(" ")[::-1], parent=curr_folder)
        curr_folder.children.append(file)
        curr_folder.add_size(int(file.size))


def find_folder(name, directory):
    folders = list(filter(lambda f: isinstance(f, Folder) and f.name == name, directory.children))
    if len(folders) == 1:
        return folders[0]
    return None


def read_input():
    is_ls = False
    for line in text.split("\n")[1:]:
        line = line.strip()

        if line.startswith("$ cd"):
            is_ls = False
            cd(line)

        if line.startswith("$ ls"):
            is_ls = True
            continue

        if is_ls:
            add_file(line)


def part_one(folder):
    size_sum = 0
    for f in folder.children:
        if isinstance(f, Folder):
            size_sum += part_one(f)
            if f.size <= 100_000:
                size_sum += f.size
    return size_sum


def part_two(folder):
    dirs = []
    for f in folder.children:
        if isinstance(f, Folder):
            dirs += part_two(f)
            if f.size >= 30_000_000 - (70_000_000 - root.size):
                dirs.append(f)
    return dirs


if __name__ == '__main__':
    read_input()
    print(f"Sum: {part_one(root)}")
    print(f"Folder to delete: {sorted(part_two(root))[0]}")
