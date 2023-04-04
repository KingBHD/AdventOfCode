def get_inputs():
    with open('input', 'r') as f:
        return f.read().splitlines()


class Day9:

    def __init__(self):
        self.head = [0, 0]
        self.tail = [0, 0]

        self.head_visited = []
        self.tail_visited = []

    @property
    def is_tail_touching(self) -> bool:
        if self.head[0] in [
            self.tail[0] - 1, self.tail[0], self.tail[0] + 1
        ] and self.head[1] in [
            self.tail[1] - 1, self.tail[1], self.tail[1] + 1
        ]:
            return True
        return False

    def move_tail(self, last=False):
        if not self.is_tail_touching or last:
            self.tail_visited.append((self.tail[0], self.tail[1]))

            self.tail[0] = self.head_visited[-1][0]
            self.tail[1] = self.head_visited[-1][1]

    def move_u(self, step: int):
        for _ in range(step):
            self.head_visited.append((self.head[0], self.head[1]))
            self.head[1] += 1
            self.move_tail()

    def move_r(self, step: int):
        for _ in range(step):
            self.head_visited.append((self.head[0], self.head[1]))
            self.head[0] += 1
            self.move_tail()

    def move_d(self, step: int):
        for _ in range(step):
            self.head_visited.append((self.head[0], self.head[1]))
            self.head[1] -= 1
            self.move_tail()

    def move_l(self, step: int):
        for _ in range(step):
            self.head_visited.append((self.head[0], self.head[1]))
            self.head[0] -= 1
            self.move_tail()


def main():
    day9 = Day9()

    for move in get_inputs():
        direction, step = move.split(' ')
        func = day9.__getattribute__(f'move_{direction.lower()}')
        func(int(step))

    day9.head_visited.append((day9.head[0], day9.head[1]))
    day9.move_tail(last=True)

    # print(day9.head_visited)
    # print(day9.tail_visited)

    print(f"Head Visited: {len(set(day9.head_visited))}")
    print(f"Tail Visited: {len(set(day9.tail_visited))}")


if __name__ == '__main__':
    main()
