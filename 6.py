import utils


def distinct_location(count):
    for i in range(len(text)-count):
        if len(set(text[i:i+count])) == count:
            return i+count
    return -1


if __name__ == '__main__':
    text = utils.get_input("6.txt")

    start_of_packet = distinct_location(4)
    message = distinct_location(14)

    print(f"Start of packet index:\t{start_of_packet}")
    print(f"Message index:\t\t\t{message}")
