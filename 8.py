import utils


def init_grid():
    g = []
    for line in text.split("\n"):
        g.append([])
        for n in line:
            g[-1].append(int(n))
    return g


def is_line_visible(tree, line):
    for other in line:
        if other >= tree:
            return False
    return True


def is_visible(tree, *directions):
    for line in directions:
        if is_line_visible(tree, line):
            return True
    return False


def calc_scenic_score(tree, *directions):
    score = 1
    for line in directions:
        score *= line_value(tree, line)
    return score


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
    height, width = len(grid), len(grid[0])
    visible_trees = height * 2 + width * 2 - 4

    max_score = 0
    for x in range(1, len(grid) - 1):
        for y in range(1, len(grid[x]) - 1):
            tree = grid[x][y]
            up, down, left, right = get_directions(x, y)

            if is_visible(tree, up, down, left, right):
                visible_trees += 1

            scenic_score = calc_scenic_score(tree, up, down, left, right)
            if scenic_score > max_score:
                max_score = scenic_score

    print(f"Visible trees:\t\t{visible_trees}")
    print(f"Max scenic score:\t{max_score}")


if __name__ == '__main__':
    text = utils.get_input("8.txt")
    grid = init_grid()
    run()
