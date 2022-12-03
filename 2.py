text = """
A Y
B Z
C Y
B Y
A X
A Y
"""


def get_val(c):
    return (ord(c) - 65) % 23


def is_tie(me: int, enemy: int):
    return me == enemy


def is_win(me: int, enemy: int):
    return not is_tie(me, enemy) and \
        (me + 1) % 3 != enemy


points = 0
for line in text.strip().split("\n"):
    enemy = get_val(line[0])
    me = get_val(line[2])

    points += (me + 1)
    if is_tie(me, enemy): points += 3
    elif is_win(me, enemy): points += 6

print(points)