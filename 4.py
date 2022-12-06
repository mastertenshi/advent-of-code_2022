class Range:
    def __init__(self, start, end) -> None:
        self.start = int(start)
        self.end = int(end)

    def is_subrange(self, range):
        return (self.start >= range.start) and (self.end <= range.end)

    def is_overlapping(self, range):
        return not (
            (self.end > range.start and self.start > range.end) or
            (self.end < range.start and self.start < range.end))


text = """
2-4,6-8
2-3,4-5
5-7,7-9
2-8,3-7
6-6,4-6
2-6,4-8
""".strip()

subrange_counter = 0
overlap_counter = 0
for line in text.split('\n'):
    first, second = line.split(',')
    first_range = Range(*first.split('-'))
    second_range = Range(*second.split('-'))

    if first_range.is_subrange(second_range) or \
       second_range.is_subrange(first_range):
        subrange_counter += 1

    if first_range.is_overlapping(second_range):
        overlap_counter += 1

print(subrange_counter)
print(overlap_counter)
