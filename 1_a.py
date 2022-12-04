text = """
100
200

500

1000

500
700
"""

max = 0
sum = 0

for line in text.split("\n"):
    if line.strip() != '':
        sum += int(line)
    else: 
        if sum > max: 
            max = sum
        sum = 0

print(max)
