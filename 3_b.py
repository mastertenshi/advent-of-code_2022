text = """
vJrwpWtwJgWrhcsFMMfFFhFp
jqHRNqRjqzjGDLGLrsFMfFZSrLrFZsSL
PmmdzqPrVvPwwTWBwg
wMqvLMZHhHMvwLHjbvcjnnSBnvTQFn
ttgJtRGJQctTZtZT
CrZsJsPPZsGzwwsLwLmpwMDw
"""

def find_common_char(x, y, z):
    for c in x:
        if c in y and c in z:
            return c


sum = 0
groups = []
for line in text.strip().split("\n"):
    groups.append(line)
    if len(groups) != 3:
        continue
    
    common_char = find_common_char(*groups)
    if common_char.islower():
        # a-z 1-26
        sum += ord(common_char) - 96
    else:
        # A-Z 27-52
        sum += ord(common_char) - 38
        
    groups.clear()


print(sum)
