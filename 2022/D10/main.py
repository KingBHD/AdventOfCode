def get_inputs():
    with open('input', 'r') as f:
        return f.read().splitlines()


class Day10:

    def __init__(self):
        self.x = 1

        self.crt_count = 0
        self.cycle_count = 0
        self.cycle_multiplexer = []

    @property
    def part_one(self):
        return sum(self.cycle_multiplexer)

    def run_instruction(self, total_cycle: int, value: int):
        for cycle in range(total_cycle):
            if self.crt_count in [self.x - 1, self.x, self.x + 1]:
                print('#', end='')
            else:
                print('.', end='')

            self.cycle_count += 1
            self.crt_count += 1

            if self.cycle_count % 40 == 20:
                self.cycle_multiplexer.append(self.cycle_count * self.x)

            if self.cycle_count % 40 == 0:
                print('')
                self.crt_count = 0

            if cycle == 1:
                self.x += value


def main():
    day10 = Day10()

    for instruct in get_inputs():
        cmd, value = instruct.split(' ') if instruct != 'noop' else ['noop', 0]

        if cmd == 'noop':
            day10.run_instruction(1, 0)

        if cmd == 'addx':
            day10.run_instruction(2, int(value))

    print(f"Part One: {day10.part_one}")
    print(f"Part Two: See the Output Above")  # EKRHEPUZ


if __name__ == '__main__':
    main()
