from utils import get_input


def get_max(elf_count):
    sum_list = [0]
    for line in text.split("\n"):
        if line.strip() != '':
            sum_list[-1] += int(line)
        else:
            sum_list.append(0)
    sum_list.sort()

    top_sum = 0
    for elf_max in sum_list[-elf_count:]:
        top_sum += elf_max

    return top_sum


if __name__ == '__main__':
    text = get_input("1.txt")
    max_elf = get_max(1)
    max_top_3 = get_max(3)

    print(f"Most calories (1) Elf:\t {max_elf}")
    print(f"Most calories (3) Elves: {max_top_3}")
