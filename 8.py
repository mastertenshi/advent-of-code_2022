import utils

text = utils.get_input("8.txt")
grid = []


def init_grid():
    global grid
    grid = []

    for line in text.split("\n"):
        grid.append([])
        for n in line:
            grid[-1].append(int(n))


def is_visible(tree, line):
    for other in line:
        if other >= tree:
            return False
    return True


def line_value(tree, line):
    count = 0
    for other in line:
        count += 1
        if other >= tree:
            return count
    return count


def flat_map(matrix, i):
    return [line[i] for line in matrix]


def get_directions(x, y):
    left = grid[x][0:y]
    right = grid[x][y + 1:]
    up = flat_map(grid[0:x], y)
    down = flat_map(grid[x + 1:], y)
    left.reverse()
    up.reverse()

    return [up, down, left, right]


def run():
    init_grid()
    height, width = len(grid), len(grid[0])
    visible_trees = height * 2 + width * 2 - 4

    max_score = 0
    for x in range(1, len(grid) - 1):
        for y in range(1, len(grid[x]) - 1):
            tree = grid[x][y]
            up, down, left, right = get_directions(x, y)

            if is_visible(tree, left) or is_visible(tree, right) or \
               is_visible(tree, up) or is_visible(tree, down):
                visible_trees += 1

            scenic_score = line_value(tree, left) * line_value(tree, right) * \
                           line_value(tree, up) * line_value(tree, down)

            if scenic_score > max_score:
                max_score = scenic_score

    print(f"Visible trees: {visible_trees}")
    print(f"Max scenic score: {max_score}")


run()
