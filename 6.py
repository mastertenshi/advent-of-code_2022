import utils

text = utils.get_input("6.txt")


def distinct_location(count):
    for i in range(len(text)-count):
        if len(set(text[i:i+count])) == count:
            return i+count
    return -1


start_of_packet = distinct_location(4)
message = distinct_location(14)

print(start_of_packet)
print(message)
