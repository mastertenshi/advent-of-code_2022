text = """
100
200

500

1000

500
700
"""

max = 0
val = 0

for line in text.split("\n"):
    if line.strip() == '':
        if val > max:
            max = val
        val = 0
    else:
        val += int(line)

print(max)
