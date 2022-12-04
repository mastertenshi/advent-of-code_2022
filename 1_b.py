text = """
100
200

500

1000

500
700
"""

sum_list = [0]
for line in text.split("\n"):
    if line.strip() != '':
        sum_list[-1] += int(line)
    else:
        sum_list.append(0)


sum_list.sort()

sum = 0
for max in sum_list[-3:]:
    sum += max

print(sum)
