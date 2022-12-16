from models import Monkey
import utils
import math


def parse_items(line):
    return [int(item) for item in line.split(':')[1].split(', ')]


def parse_op(line):
    return eval(f"lambda old: {line.split('=')[1]}")


def parse_test(line):
    return lambda x: x % int(line[line.rindex(' '):]) == 0


def parse_throw(line):
    return int(line[line.rindex(' '):])


def monkey_business():
    for _ in range(20):
        for monkey in monkeys:
            for item in monkey.items:
                monkey.inspection_count += 1
                item = monkey.op(item) // 3
                if monkey.test(item):
                    monkeys[monkey.if_true].items.append(item)
                else:
                    monkeys[monkey.if_false].items.append(item)
            monkey.items = []


if __name__ == '__main__':
    lines = utils.get_input('11.txt').split('\n')
    monkeys = []

    for i in range(0, len(lines), 7):
        monkeys.append(Monkey(
            parse_items(lines[i + 1]),
            parse_op(lines[i + 2]),
            parse_test(lines[i + 3]),
            parse_throw(lines[i + 4]),
            parse_throw(lines[i + 5]),
        ))

    monkey_business()

    monkeys.sort(key=lambda m: m.inspection_count)
    print(math.prod(list(map(lambda m: m.inspection_count, monkeys[-2:]))))
