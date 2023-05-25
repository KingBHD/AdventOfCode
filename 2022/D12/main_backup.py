from collections import defaultdict
from copy import deepcopy
from string import ascii_lowercase


class Day12:

    def __init__(self):
        self.heightmap = []
        self.start = ()
        self.end = ()
        self.blacklist = []

    @staticmethod
    def get_inputs():
        with open('input', 'r') as f:
            return f.read().splitlines()

    def read_heightmap(self):
        for idx, row in enumerate(self.get_inputs()):
            self.heightmap.append(list(row))
            if 'S' in row:
                self.start = (idx, row.find('S'))

            if 'E' in row:
                self.end = (idx, row.find('E'))

    def get_height(self, x, y):
        return ascii_lowercase.find(self.heightmap[x][y]) + 1

    def get_nears(self, start):
        nears = []
        t__x = start[0] - 1
        if t__x >= 0:
            nears.append(((t__x, start[1]), 'v'))

        b__x = start[0] + 1
        if b__x < len(self.heightmap):
            nears.append(((b__x, start[1]), '^'))

        l__y = start[1] - 1
        if l__y >= 0:
            nears.append(((start[0], l__y), '<'))

        r__y = start[1] + 1
        if r__y < len(self.heightmap[0]):
            nears.append(((start[0], r__y), '>'))
        return nears

    def find_path(self, path, point, visited):
        if point in visited:
            return [], visited
        nears = self.get_nears(point)
        for poi in path:
            nears.remove(poi) if poi in nears else None

        candidates = defaultdict(list)
        value = self.get_height(*point)
        for n in nears:
            new_value = self.get_height(*n)
            if value in [new_value, new_value - 1]:
                candidates[str(new_value)].append(n)

        print(f"Exploring {self.heightmap[point[0]][point[1]]} {point} from {path[-1]}", dict(candidates))

        path_value = []
        if len(candidates.keys()) > 0:
            for opt in candidates[max(candidates.keys())]:
                new_path = deepcopy(path)
                new_path.append(point)
                forward_path, visited = self.find_path(new_path, opt[0], visited + [point])
                path_value = min([path_value, forward_path])

        return path_value, visited

    def main(self):
        self.read_heightmap()
        path = self.find_path([self.start], self.start, [])
        # print(len(path))


if __name__ == '__main__':
    day12 = Day12()
    try:
        day12.main()
    except RecursionError:
        print('RecursionError')
