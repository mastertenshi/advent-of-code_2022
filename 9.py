from models import Node
import utils


def init(rope_length):
    node = H
    for _ in range(rope_length):
        child = Node(parent=node)
        node.child = child
        node = child

    node.child = T
    T.parent = node


def run(rope_length):
    init(rope_length)

    for line in text.split("\n"):
        line = line.split(' ')
        direction, moves = line[0], int(line[1])
        for _ in range(moves):
            move(direction)


def move(direction):
    H.move(*{
        'R': (0, 1),
        'L': (0, -1),
        'U': (1, 0),
        'D': (-1, 0)
    }[direction])

    parent = H
    while parent.child is not None:
        child = parent.child
        # Delta
        dx, dy = parent.x - child.x, parent.y - child.y
        if abs(dx) > 1 or abs(dy) > 1:
            child.move(move_distance(dx), move_distance(dy))
        parent = child

    visited.add((T.x, T.y))


def move_distance(delta):
    if delta == 0:
        return 0
    return delta // abs(delta)


if __name__ == '__main__':
    text = utils.get_input("9.txt")
    visited = set()
    H, T = Node(), Node()

    run(rope_length=8)
    print(len(visited))
