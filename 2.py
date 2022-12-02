text = """
A Y
B Z
C Y
B Y
A Y
A Y
"""

def getVal(c):
    return (ord(c) - 65) % 23

def isTie(me, enemy):
    return me == enemy

def isWin(me, enemy):
    return (me + 1) % 3 != enemy

points = 0
for line in text.strip().split("\n"):
    enemy = getVal(line[0])
    me = getVal(line[2])

    points += (me + 1)
    if isTie(me, enemy): points += 3
    elif isWin(me, enemy): points += 6

print(points)
