from utils import get_input

text = get_input("2.txt")


def get_val(c):
    return (ord(c) - 65) % 23


def is_tie(me: int, enemy: int):
    return me == enemy


def is_win(me: int, enemy: int):
    return not is_tie(me, enemy) and \
        (me + 1) % 3 != enemy


def play(should_calculate_move):
    points = 0
    for line in text.strip().split("\n"):
        enemy = get_val(line[0])
        me = get_val(line[2])

        if should_calculate_move:
            me = (enemy + me - 1) % 3
            if me == -1:
                me = 2

        points += (me + 1)
        if is_tie(me, enemy):
            points += 3
        elif is_win(me, enemy):
            points += 6
    return points


part_one = play(False)
part_two = play(True)

print(part_one)
print(part_two)
