from collections import defaultdict


def get_inputs():
    with open('input', 'r') as f:
        return f.read().splitlines()


class Day9:

    def __init__(self):
        self.rope = [
            [0, 0],  # head
            [0, 0],  # tail-1
            [0, 0],  # tail-2
            [0, 0],  # tail-3
            [0, 0],  # tail-4
            [0, 0],  # tail-5
            [0, 0],  # tail-6
            [0, 0],  # tail-7
            [0, 0],  # tail-8
            [0, 0],  # tail-9
        ]

        self.visited = defaultdict(list)

    @staticmethod
    def is_tail_touching(head, tail) -> bool:
        if head[0] in [
            tail[0] - 1, tail[0], tail[0] + 1
        ] and head[1] in [
            tail[1] - 1, tail[1], tail[1] + 1
        ]:
            return True
        return False

    def move_tail(self, last=False):
        for idx, node in enumerate(self.rope[1:], start=1):
            head = 'head' if idx == 1 else f'tail-{idx - 1}'
            tail = f'tail-{idx}'

            if not self.is_tail_touching(self.rope[idx - 1], node) or last:
                self.visited[tail].append((node[0], node[1]))
                self.rope[idx] = self.visited[head][-1]

    def move_u(self, step: int):
        for _ in range(step):
            self.visited['head'].append((self.rope[0][0], self.rope[0][1]))
            self.rope[0][1] += 1
            self.move_tail()

    def move_r(self, step: int):
        for _ in range(step):
            self.visited['head'].append((self.rope[0][0], self.rope[0][1]))
            self.rope[0][0] += 1
            self.move_tail()

    def move_d(self, step: int):
        for _ in range(step):
            self.visited['head'].append((self.rope[0][0], self.rope[0][1]))
            self.rope[0][1] -= 1
            self.move_tail()

    def move_l(self, step: int):
        for _ in range(step):
            self.visited['head'].append((self.rope[0][0], self.rope[0][1]))
            self.rope[0][0] -= 1
            self.move_tail()


def main():
    day9 = Day9()

    for move in get_inputs():
        direction, step = move.split(' ')
        func = day9.__getattribute__(f'move_{direction.lower()}')
        func(int(step))

    day9.visited['head'].append((day9.rope[0][0], day9.rope[0][1]))
    day9.move_tail(last=True)

    print(day9.visited)

    print(f"Head Visited: {len(set(day9.visited['head']))}")
    print(f"Tail Visited: {len(set(day9.visited['tail-9']))}")


if __name__ == '__main__':
    main()
