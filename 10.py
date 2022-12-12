import utils


def do_cycle(count):
    global cycle, signal_strength_sum

    for _ in range(count):
        cycle += 1

        x = register['x']
        if cycle % 40 in range(x, x + 3):
            CRT.append('#')
        else:
            CRT.append('.')

        if (cycle - 20) % 40 == 0:
            signal_strength = register['x'] * cycle
            signal_strength_sum += signal_strength

            print(f"Cycle {cycle}: {signal_strength}")


def print_crt():
    for i in range(len(CRT)):
        if i % 40 == 0:
            print()
        print(CRT[i], end='')


if __name__ == '__main__':
    text = utils.get_input("10.txt")
    signal_strength_sum = 0
    register = {'x': 1}
    cycle = 0
    CRT = []

    for line in text.split('\n'):
        if line.startswith("noop"):
            do_cycle(1)

        elif line.startswith("add"):
            do_cycle(2)
            r, value = line.removeprefix("add").split(' ')
            register.setdefault(r, 1)
            register[r] += int(value)

    print(f"\nSum: {signal_strength_sum}")
    print_crt()
