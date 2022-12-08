from models import Range
import utils


def run():
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

    print(f"Subrange count:\t{subrange_counter}")
    print(f"Overlap count:\t{overlap_counter}")


if __name__ == '__main__':
    text = utils.get_input("4.txt")
    run()
