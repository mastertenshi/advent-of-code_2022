text = """
vJrwpWtwJgWrhcsFMMfFFhFp
jqHRNqRjqzjGDLGLrsFMfFZSrLrFZsSL
PmmdzqPrVvPwwTWBwg
wMqvLMZHhHMvwLHjbvcjnnSBnvTQFn
ttgJtRGJQctTZtZT
CrZsJsPPZsGzwwsLwLmpwMDw
"""

def find_common_char(first_half, second_half):
    for c in first_half:
        if c in second_half:
            return c

sum = 0
for line in text.strip().split("\n"):
    center = len(line) // 2
    first_half, second_half = line[0:center], line[center:]
    
    common_char = find_common_char(first_half, second_half)
    if common_char.islower():
        # a-z 1-26
        sum += ord(common_char) - 96
    else:
        # A-Z 27-52
        sum += ord(common_char) - 38


print(sum)
