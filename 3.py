import utils


text = utils.get_input("3.txt")


def find_common_char(string, *strings):
    for c in string:
        is_common = True
        for other_string in strings:
            if c not in other_string:
                is_common = False
        if is_common:
            return c


def get_value(common_char):
    if common_char.islower():
        return ord(common_char) - 96  # a-z 1-26
    return ord(common_char) - 38      # A-Z 27-52


def run():
    elf_sum = 0
    group_sum = 0
    groups = []
    for line in text.strip().split("\n"):
        # Elf sum
        center = len(line) // 2
        first_half, second_half = line[0:center], line[center:]
        elf_sum += get_value(find_common_char(first_half, second_half))

        # Group sum
        groups.append(line)
        if len(groups) == 3:
            group_sum += get_value(find_common_char(*groups))
            groups.clear()

    print(f"Elf sum:\t{elf_sum}")
    print(f"Group sum:\t{group_sum}")


run()
