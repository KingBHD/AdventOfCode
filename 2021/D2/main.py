def get_my_input():
    raw_lines = open('input', 'r').readlines()
    return raw_lines


def part_one():
    forward = 0
    depth = 0

    instructions = get_my_input()
    for instruction in instructions:
        inst, val = instruction.split(' ')
        if inst == 'forward':
            forward += int(val)
        elif inst == 'down':
            depth += int(val)
        elif inst == 'up':
            depth -= int(val)

    print(forward, depth)
    print(forward * depth)


def part_two():
    forward = 0
    depth = 0
    aim = 0
    instructions = get_my_input()
    for instruction in instructions:
        inst, val = instruction.split(' ')
        if inst == 'down':
            aim += int(val)
        elif inst == 'up':
            aim -= int(val)
        elif inst == 'forward':
            forward += int(val)
            depth += int(val) * aim

    print(forward, depth)
    print(forward * depth)


def main():
    part_two()


if __name__ == '__main__':
    main()
