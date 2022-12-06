from pprint import pprint
import re


def get_input():
    with open("input/5.txt", "r") as file:
        return file.read()


def get_stacks_count(text):
    for line in text.split('\n'):
        if line.strip().startswith('1'):
            return int(line[line.strip().rfind(' '):].strip())
    return -1


def get_stacks(text):
    stacks = [[] for _ in range(get_stacks_count(text))]
    
    for line in text.split('\n'):
        if not line.strip().startswith('['): break
        
        for i in range(1, len(line), 4):
            if line[i] != ' ': stacks[(i-1) // 4].append(line[i])
        
    for i in range(0, len(stacks)):
        stacks[i].reverse()
        
    return stacks


def move_elements_first(stacks, text):
    for line in text.split('\n'):
        if line.startswith('move'):
            [move_count, fr0m, to] = list(map(lambda c: int(c), re.findall('\d+', line)))
            for _ in range(move_count):
                stacks[to-1].append(stacks[fr0m-1].pop())
    return stacks


def move_elements_second(stacks, text):
    for line in text.split('\n'):
        if line.startswith('move'):
            [move_count, fr0m, to] = list(map(lambda c: int(c), re.findall('\d+', line)))
            stacks[to-1] += stacks[fr0m-1][-move_count:]
            stacks[fr0m-1] = stacks[fr0m-1][0:-move_count]
    return stacks


text = get_input()
stacks_first = move_elements_first(get_stacks(text), text)
stacks_second = move_elements_second(get_stacks(text), text)

pprint(stacks_first)
pprint(stacks_second)
