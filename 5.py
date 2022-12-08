from pprint import pprint
import utils
import re

text = utils.get_input("5.txt")


def get_stacks_count():
    for line in text.split('\n'):
        if line.strip().startswith('1'):
            return int(line[line.strip().rfind(' '):].strip())
    return -1


def get_stacks():
    stacks = [[] for _ in range(get_stacks_count())]

    for line in text.split('\n'):
        if not line.strip().startswith('['): break

        for i in range(1, len(line), 4):
            if line[i] != ' ':
                stacks[(i - 1) // 4].append(line[i])

    for i in range(0, len(stacks)):
        stacks[i].reverse()

    return stacks


def move_stacks():
    stacks_1 = get_stacks()
    stacks_2 = get_stacks()

    for line in text.split('\n'):
        if line.startswith('move'):
            [move_count, src, dest] = list(map(lambda c: int(c), re.findall('\\d+', line)))
            src -= 1
            dest -= 1

            # First method  (normal stack)
            for _ in range(move_count):
                stacks_1[dest].append(stacks_1[src].pop())

            # Second method  (move multiple elements at a time)
            stacks_2[dest] += stacks_2[src][-move_count:]  # add to destination
            stacks_2[src] = stacks_2[src][0:-move_count]   # remove from source

    return stacks_1, stacks_2


first, second = move_stacks()

print("First method----")
pprint(first)

print("\nSecond method----")
pprint(second)
