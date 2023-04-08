import math
from collections import defaultdict


def get_inputs():
    with open('input', 'r') as f:
        return f.read().splitlines()


class Day9:

    def __init__(self):
        self.rope = defaultdict(list)
        self.rope['tail-0'] = [(0, 0)]
        self.rope['tail-1'] = [(0, 0)]
        self.rope['tail-2'] = [(0, 0)]
        self.rope['tail-3'] = [(0, 0)]
        self.rope['tail-4'] = [(0, 0)]
        self.rope['tail-5'] = [(0, 0)]
        self.rope['tail-6'] = [(0, 0)]
        self.rope['tail-7'] = [(0, 0)]
        self.rope['tail-8'] = [(0, 0)]
        self.rope['tail-9'] = [(0, 0)]

    @staticmethod
    def get_neighbours(node):
        return [
            (node[0] - 1, node[1] + 1), (node[0] + 1, node[1] + 1),
            (node[0] - 1, node[1] - 1), (node[0] + 1, node[1] - 1),
            (node[0], node[1] + 1), (node[0] + 1, node[1]),
            (node[0], node[1] - 1), (node[0] - 1, node[1]),
        ]

    @staticmethod
    def is_tail_touching(head, tail) -> bool:
        if head[0] in [
            tail[0] - 1, tail[0], tail[0] + 1
        ] and head[1] in [
            tail[1] - 1, tail[1], tail[1] + 1
        ]:
            return True
        return False

    def get_closest_commons(self, node_one, node_two):
        return set(
            self.get_neighbours(node_one)
        ).intersection(
            self.get_neighbours(node_two)
        )

    def get_closest(self, tail, head):
        commons__ = self.get_closest_commons(head, tail)
        distance = {coord: math.dist(head, coord) for coord in commons__}
        return sorted(distance.items(), key=lambda x: x[1])[0][0]

    def move_tail(self, last=False):
        for idx in range(10):
            if idx == 0:
                continue

            head = self.rope[f'tail-{idx - 1}'][-1]
            tail = self.rope[f'tail-{idx}'][-1]

            if not self.is_tail_touching(head, tail) or last:
                self.rope[f'tail-{idx}'].append(self.get_closest(tail, head))

    def move_in(self, direction: str):
        head = self.rope['tail-0'][-1]

        if direction == 'U':
            head = (head[0], head[1] + 1)
        if direction == 'R':
            head = (head[0] + 1, head[1])
        if direction == 'D':
            head = (head[0], head[1] - 1)
        if direction == 'L':
            head = (head[0] - 1, head[1])

        self.rope['tail-0'].append(head)
        self.move_tail()


def main():
    day9 = Day9()

    for move in get_inputs():
        direction, step = move.split(' ')

        for _ in range(int(step)):
            day9.move_in(direction)

    print(f"1st Tail (Part One): {len(set(day9.rope['tail-1']))}")
    print(f"9th Tail (Part Two): {len(set(day9.rope['tail-9']))}")


if __name__ == '__main__':
    main()
