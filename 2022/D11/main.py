import math
from collections import defaultdict
from typing import Callable


def get_inputs():
    with open('input', 'r') as f:
        return f.read().splitlines()


class Day11:

    def __init__(self):
        self.monkeys = defaultdict(list)
        self.operations = defaultdict(Callable)
        self.test = defaultdict(Callable)

    def build_monkey(self):
        on_monkey = '0'
        divisor = 0
        if_true = 0
        if_false = 0

        for instruct in get_inputs():
            if instruct.startswith(f"Monkey "):
                _, no = instruct.split(' ')
                on_monkey = no[:-1]
                continue

            if instruct.startswith("  Starting items: "):
                self.monkeys[on_monkey] = list(map(int, instruct[17:].split(',')))
                continue

            if instruct.startswith("  Operation: "):
                exp = instruct[18:].format(old=0)
                self.operations[on_monkey] = eval(f"lambda old: {exp}")
                continue

            if instruct.startswith("  Test: divisible by "):
                divisor = int(instruct[20:])
                continue

            if instruct.startswith("    If true: throw to monkey "):
                if_true = int(instruct[28:])
                continue

            if instruct.startswith("    If false: throw to monkey "):
                if_false = int(instruct[29:])
                self.test[on_monkey] = eval(f"lambda new: {if_true} if new % {divisor} == 0 else {if_false}")

    def main(self):
        self.build_monkey()
        active = defaultdict(int)
        for _ in range(10000):
            print("Round:", _)
            for monkey in range(len(self.monkeys.keys())):

                for old in self.monkeys[str(monkey)]:
                    new = math.floor(self.operations[str(monkey)](old))
                    # new = math.floor(new / 3)

                    active[str(monkey)] += 1
                    to_monkey = self.test[str(monkey)](new)
                    self.monkeys[str(to_monkey)].append(new)

                self.monkeys[str(monkey)] = []

        print(active)
        a, b = sorted(active.values(), reverse=True)[:2]
        print(a * b)


if __name__ == '__main__':
    day11 = Day11()
    day11.main()
